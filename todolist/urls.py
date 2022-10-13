from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import delete_task
from todolist.views import add_todolist
from todolist.views import show_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/',  logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('delete-task/<int:id>', delete_task, name='delete-task'),
    path('json/', show_json, name='show_json'),
    path('add/', add_todolist, name='add_todolist'),
]