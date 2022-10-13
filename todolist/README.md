### Link apk
```
https://projek-pbp.herokuapp.com/todolist/
```

# Tugas 4 PBP

**1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?**
CSRF merupakan singkatan dari Cross Site Request Forgery berguna untuk mencegah serangan CSRF yang membuat penyerang tidak mungkin melakukan *request* HTTP yang keseluruhannya valid yang cocok untuk diumpamakan ke korban. Jika tidak ada `csrf_token` maka website akan rentan terhadap *cyber attack*.

**2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.**
Kita bisa membuat form secara manual dengan cara, ambil contoh dari fungsi create_task
```
<form method="POST" action="">

    {% csrf_token %}

    <table>
        <tr>
            <td>Date: </td>
            <td><input type="date" name="date" placeholder="DATE" class="form-control"></td>
        </tr>

        <tr>
            <td>Tittle: </td>
            <td><input type="text" name="title" placeholder="TITTLE" class="form-control"></td>
        </tr>

        <tr>
            <td>Description: </td>
            <td><input type="text" name="description" placeholder="DESCRIPTION" class="form-control"></td>
        </tr>

        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Submit" href="{% url 'todolist:show_todolist' %}"></td>
        </tr>
    </table>

</form>
```
lalu pada `views.py` kita membuat 
```
def create_task(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = request.POST.get("date")
        user = request.user
        data = Task(user = user, title=title, description=description, date=date)
        data.save()
        return redirect("todolist:show_todolist")
    return render(request, "create_task.html", context)
```
**3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**
Setelah *user* mengisi form maka data akan diteruskan ke `views.py` yang berisi atribut dari data. Lalu dibuat instance dari model baru berdasarkan atribut yang ada. Setelah itu disimpan ke database. Instance yang sudah ada di database akan ditampilkan di HTML.

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. Membuat app baru `todolist`
`python manage.py startapp todolist`

2. Menambahkan aplikasi pada `settings.py` dan `urls.py` pada folder `project_djago`. Lalu menambahkan path pada `urlpatterns` di `urls.py`

3. Pada `models.py` buat objek Task yang memiliki atribut user, date, title, description
```
class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
        )
    date = models.TextField()
    title = models.TextField()
    description = models.TextField()
```

4. Pada `views.py` buat fungsi
`register`, `login_user`, dan `logout_user`. Pada fungsi inti saya membuat form dengan cara
`form = UserCreationForm()`pada fungsi register untuk melakukan registrasi akun. Jika sudah memiliki akun, *user* akan mencoba login. Pada fungsi login_user akan dicek apakah akun sudah terdaftar atau belum.
Selanjutnya buat file HTML untuk register dan login yang akan mengimplementasikan form yang tadi dibuat agar ditampilkan ke browser.

5. buat file HTML `todolist.html` yang berisi username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
```
{% extends 'base.html' %}

{% block content %}
<title>To Do List</title>

<h5>Username: {{username}}</h5>


<table>
{% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    <tr>
    <th>date</th>
    <th>title</th>
    <th>description</th>
    </tr>
    {% for data in list_todo %}
    <tr>
        <th>{{data.date}}</th>
        <th>{{data.title}}</th>
        <th>{{data.description}}</th>
    </tr>
{% endfor %}
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
</table>
<h5>Sesi terakhir login: {{ last_login }}</h5>
<button><a href="{% url 'todolist:logout' %}">Logout</a></button>
<button><a href="{% url 'todolist:create_task' %}">create_task</a></button>

{% endblock content %}
```

6. Tambahkan fungsi `create_task` pada `views.py` untuk membuat form yang berisi judul task dan deskripsi task.

7. Melakukan routing dengan menambahkan `urlpatterns` pada `urls.py` yang ada pada folder todolist
```
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
]
```

8. Buka `Settings -> Secrets -> Actions -> new repository secrets`. Lalu buka heroku dan copy `API` dan `nama projek aplikasi`, lalu tambahkan ke dalam repository secret. Setelah selesai jangan lupa untuk simpan perubahan.

9. Setelah deploy heroku, kita jalankan app nya dan membuat 2 akun baru yang berisi 3 data. Untuk melihat data bisa di `admin`.

# Tugas 5 PBP

**1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**
->Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML.    Setiap elemen HTML memiliki atribut `style`.
Kelebihan:
- proses load website cepat
- lebih mudah dalam *fix code* jika terjadi kesalahan
Kekurangan:
- kurang cocok jika ingin membuat style yang akan dipakai lagi.

-> Internal CSS adalah kode yang ditulis menggunakan `<style>` sehingga dapat mendefinisikan *styling* dari selector.
Kelebihan:
- class dan ID bisa dipakai oleh internal stylesheet
- Perubahan CSS hanya satu *page* saja
Kekurangan:
- Jika style yang dibuat banyak maka akan memenuhi template.

-> Eksternal CSS adalah kode CSS yang ditulis terpisah dari file HTML menggunakan `.css`
Kelebihan:
- file `.css` dapat digunakan beberapa template
Kekurangan:
- Memengaruhi waktu render website karena mengambil file dari luar.

**2. Jelaskan tag HTML5 yang kamu ketahui.**
`h1` -- `h6` akan menamilkan teks dengan `h1` ukuran terbesar dan bertambahnya  angka membuat ukuran teks makin kecil
`p` menampilkan teks berukuran normal
`a` Teks yang diapit akan muncul sebagai link
`button` membuat button
`div` membungkus dan memisahkan elemen lain
`form` mendefinisikan form input
`nav` mendefinisikan navbar
`video` menambahkan video di HTML
`input` digunakan dalam tag `form` untuk mengambil input dari *user*.

**3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.**
1. Elemen selector
   Element selector menggunakan tag HTML sebagai selector untuk mengubah properti yang terdapat dalam tag tersebut.
```
h1 {
  color: #fca205;
  font-family: "Monospace";
  font-style: italic;
}
```

2. ID selector
   ID selector menggunakan ID pada tag sebagai selector-nya. TD yang ingin ditambahkan harus bersifat unik
```
...
<body>
  <div id="header">
    <h1>Tutorial CSS Yay</h1>
  </div>
  ...
</body>
```
kemudian pada file CSS
```
#header {
  background-color: #f0f0f0;
  margin-top: 0;
  padding: 20px 20px 20px 40px;
}
```

3. Class selector
   menggunakan class pada file HTML 
```
<div class="card-header card-bg-rv">Date: {{data.date}}</div>
```
   lalu pada file CSS
```
.card-bg-rv {
    color: rebeccapurple;
    background-color: black;
}
```

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. Mendefinisikan bootstrap pada `base.html`
```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
```
2. Kustomisasi file .html yang ada menggunakan bootstrap yang sudah saya tambahkan

3. Bonus menambahkan efek hover pada cards. Pada file `todolist.html` saya menambahkan efek zoom lalu saya menuliskannya pada file `style.css`
```
<div class="card text-center zoom">
    ...
</div>
```
file CSS
```
.zoom:hover {
    transform: scale(1.3);
}
```
