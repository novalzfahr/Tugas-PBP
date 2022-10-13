### Link apk
```
https://projek-pbp.herokuapp.com/todolist/
```

**1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
- Asynchronus programming
    - teknik dimana dapat menjalankan task secara paralel tanpa harus menunggu salah satu task selesai dahulu, bisa berjalan bersamaan. Waktu eksekusi lebih cepat.
- Synchronus programming
    - teknik dimana jika harus menjalankan task lain ketika sedang menjalankan task, maka harus menunggu task tersebut selesai dahulu jadi akan memakan waktu lebih lama.

**2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
-  Event-Driven Programming adalah salah satu teknik pemogramman, yang konsep kerjanya tergantung dari kejadian atau event tertentu. Event-Driven programming juga bisa dibilang suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya. Contoh di program: `$("#form-ajax").on("submit",function(e) {}`

**3.  Jelaskan penerapan asynchronous programming pada AJAX.**
- Menambahkan ` <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` pada base html `<head>`
- Tambahkan `<script>` di dalam file html
- Ajax akan melakukan event yang telah dibuat.
- *action* dan *response* akan dilakukan secara asynchronus oleh server
- Data akan ditampilkan pada page tanpa harus refresh lagi.

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
- Tambahkan views
```
@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Tambahkan path show_json ke urlpatterns di `urls.py`
- Tambahkan fungsi add_todolist dalam bentuk ajax
```
@csrf_exempt
@login_required(login_url="/todolist/login/")
def add_todolist(request):
    if request.method == "POST":
        title = request.POST.get("title")
        date = request.POST.get("date")
        deskripsi = request.POST.get("deskripsi")
        Task.objects.create(
            title=title, date=date, description=deskripsi, user=request.user
        )
        return JsonResponse({
            "title": title,
            "date": date,
            "deskripsi": deskripsi
        }, status=200)
```
- Tambahkan path add_todolist ke urlpatterns di `urls.py`
- Tambahkan ajax script di `base.html`
```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```
- Modifikasi dan buat fungsi GET di `todolist.html`
```
$.getJSON("{% url 'todolist:show_json' %}", function(data){
    $.each(data, function(index,value){
    console.log(value)
        $("#todolist").append(
        `<div class="card text-center zoom">
            <div class="card-header card-bg-rv">Date: ${value.fields.date}</div>
            <div class="image-box card-bg-rv">
                <img src= "/static/media/a3.png" height="200"">
                <div class="card responsive-card">
                <div class="card-body card-bg-rv">
                    <h5 class="card-title"> ${value.fields.title}</h5>
                    <p class="card-text"> ${value.fields.description} </p>
                    <a href="#" class="btn btn-primary">Delete task</a>
                </div>
                </div>
            </div>
            </div>  
        </div>`    
        )
    })
})
```
- Tambahkan modal di `todolist.html`
```
<div class="modal fade" id="modal-todolist" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5">Create task</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form id="form-ajax" action = "/todolist/add/">
          {% csrf_token %}
          <div class="mb-3">
            <label class="col-form-label">Date:</label>
            <input type="date" class="form-control" id="date" required>
          </div>
          <div class="mb-3">
            <label class="col-form-label">Title:</label>
            <input type="text" class="form-control" id="title" required>
          </div>
          <div class="mb-3">
            <label class="col-form-label">Description:</label>
            <textarea class="form-control" id="deskripsi" required></textarea>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" value="submit" class="btn btn-primary" id="btn_submit">Submit</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
```
- Tambahkan fungsi POST di `todolist.html`
```
$("#form-ajax").on("submit",function(e) {
    e.preventDefault() 
    let date = $("#date").val();
    let title = $("#title").val();
    let deskripsi = $("#deskripsi").val();
    $.ajax({
    method: "POST",
    url: "/todolist/add/",
    data: {"date":date, "title":title, "deskripsi":deskripsi},
    }).done(function(resp) {
    console.log(resp)
    $("#todolist").append(
        `<div class="card text-center zoom">
        <div class="card-header card-bg-rv">Date: ${resp.date}</div>
            <div class="image-box card-bg-rv">
            <img src= "/static/media/a3.png" height="200"">
            <div class="card responsive-card">
                <div class="card-body card-bg-rv">
                <h5 class="card-title"> ${resp.title}</h5>
                <p class="card-text"> ${resp.deskripsi} </p>
                <a id="btn-delete" class="btn btn-primary">Delete task</a>
                </div>
            </div>
            </div>
        </div>  
        </div>`    
    )
    $("#modal-todolist").modal("toggle")
    });
})
```