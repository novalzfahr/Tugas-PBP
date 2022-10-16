import operator
import datetime
from todolist.models import Task
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task= Task.objects.filter(user= request.user)
    task = sorted(task, key= operator.attrgetter('date'))
    context = {
    'list_todo': task,
    'username': request.COOKIES['username'],
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('username', username)
            response.set_cookie('last_login', str(datetime.datetime.now()))   
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

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

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_todolist')

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    response.delete_cookie('username')
    return response
