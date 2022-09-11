from django.shortcuts import render
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_katalog,
    'nama': 'Achmad Noval Fahrezi',
    'student_ID': '2106750931'
    }
    return render(request, "katalog.html", context)
