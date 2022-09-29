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

9. 


