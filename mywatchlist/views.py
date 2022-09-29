from django.shortcuts import render
from mywatchlist.models import MywatchlistItem
from django.http import HttpResponse
from django.core import serializers

# # TODO: Create your views here.
def show_mywatchlist(request):
    data_my_watch_list= MywatchlistItem.objects.all()
    watched = 0
    not_watched = 0
    for i in data_my_watch_list:
        if (i == "Iya"):
            watched += 1
        elif (i == "Tidak"):
            not_watched += 1
        
        
    if watched > not_watched:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!" 

    context = {
    'list_barang': data_my_watch_list,
    'nama': 'Achmad Noval Fahrezi',
    'student_ID': '2106750931',
    'pesan': pesan,
    }
    return render(request, "mywatchlist.html", context)

def show_html(request):
    data = MywatchlistItem.objects.all()
    context = {
    'list_barang': data,
    'nama': 'Achmad Noval Fahrezi',
    'student_ID': '2106750931'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = MywatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MywatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
