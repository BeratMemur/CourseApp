from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

data = {
    "programlama": "Programlama kategorisine ait kurslar",
    "web-gelistirme": "Web geliştrime kategorisine ait kurslar",
    "mobil": "Mobil kategorisine ait kurslar"
}

db = {
    "courses": [
        {
            "title": "javascript kursu",
            "description": "javascript kurs açıklaması",
            "imageUrl": "js.jpg",
            "slug": "javascript-kursu",
            "date": date(2024,11,22),
            "isActive": True,
            "isUpdated": True
        },
        {
            "title": "python kursu",
            "description": "python kurs açıklaması",
            "imageUrl": "python.jpg",
            "slug": "python-kursu",
            "date": date(2024,10,5),
            "isActive": True,
            "isUpdated": True

        },
        {
            "title": "web geliştirme kursu",
            "description": "web geliştirme kurs açıklaması",
            "imageUrl": "html.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2024,9,10),
            "isActive": True,
            "isUpdated": False

        }
    ],
    "categories": [
        {"id": 1, "name":"programlama", "slug": "programlama"},
        {"id": 2, "name":"web geliştirme", "slug": "web-gelistirme"},
        {"id": 3, "name":"mobil uygulamalar", "slug": "mobil"},
    ]
}

def index(request):
    courses = [course for course in db["courses"] if course["isActive"] == True]
    categories = db["categories"]

    return render(request, 'courses/index.html', {
        'courses': courses,
        'categories': categories
    })


def details(request, course_name):
    return HttpResponse(f"{course_name} detay sayfası")


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
