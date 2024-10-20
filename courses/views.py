from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

data = {
    "programlama": "Programlama kategorisine ait kurslar",
    "web-gelistirme": "Web geliştrime kategorisine ait kurslar",
    "mobil": "Mobil kategorisine ait kurslar"
}

def index(request):
    return render(request, 'courses/index.html')


def courses(request):
    category_list = list(data.keys())
    list_items = ""
    for category in category_list:
        redirect_url = reverse('courses_by_category', args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

    html = f"<h1>Kurs Listesi<h1> <br> <ul>{list_items}</ul>"

    return HttpResponse(html)


def details(request, course_name):
    return HttpResponse(f"{course_name} detay sayfası")


def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound('<h1>yanlış kategori seçimi<h1>')
    

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())

    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori seçimi")
    
    categorty_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[categorty_name])

    return redirect(redirect_url)
