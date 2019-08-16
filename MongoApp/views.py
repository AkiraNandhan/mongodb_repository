from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def home_view_page(request):
    return render(request,'home.html')





def krishna_view_page(request):
    return render(request,'krishna.html')


def WestGodavari_view_page(request):
    return render(request,'westgodavari.html')


def Eastgodavari_view_page(request):
    return render(request,'Eastgodavari.html')


def vijayawada_view_html(request):
    return HttpResponse('i love vijayawada')