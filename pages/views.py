from django.shortcuts import render
from courses.models import Course
from pages.models import Slider

def index(request):
    slider = Slider.objects.filter(isActive=1)
    courses = Course.objects.filter(isActive=1, isHome=1)

    return render(request, 'pages/index.html',{
        "slider": slider,
        "courses":courses,
    })


def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')