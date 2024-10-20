from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('anasayfa')

def courses(request):
    return HttpResponse('kurs listesi')