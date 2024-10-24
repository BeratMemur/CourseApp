from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseNotFound
from django.urls import reverse
from .models import Course, Category

data = {
    "programlama": "Programlama kategorisine ait kurslar",
    "web-gelistirme": "Web geliştrime kategorisine ait kurslar",
    "mobil": "Mobil kategorisine ait kurslar"
}

def index(request):
    courses = Course.objects.filter(isActive=1)
    categories = Category.objects.all()

    return render(request, 'courses/index.html', {
        'courses': courses,
        'categories': categories
    })


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    return render(request, 'courses/details.html',context)


def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'courses/courses.html', {
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound('<h1>yanlış kategori seçimi<h1>')
    

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())

    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori seçimi")
    
    categorty_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[categorty_name])

    return redirect(redirect_url)
