from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('anasayfa')

def communication(request):
    return HttpResponse('iletişim sayfası')

def aboutUs(request):
    return HttpResponse('hakkımızda sayfası')