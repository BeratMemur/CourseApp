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
            "imageUrl": "https://appmaster.io/api/_files/hRaLG2N4DVjRZJQzCpN2zJ/download/",
            "slug": "javascript-kursu",
            "date": date(2024,10,22),
            "isActive": False
        },
        {
            "title": "python kursu",
            "description": "python kurs açıklaması",
            "imageUrl": "https://ciracollege.com/wp-content/uploads/2020/11/How-to-Learn-Python.jpg",
            "slug": "python-kursu",
            "date": date(2024,10,9),
            "isActive": True

        },
        {
            "title": "web geliştirme kursu",
            "description": "web geliştirme kurs açıklaması",
            "imageUrl": "https://astrodijital.com/wp-content/uploads/2023/09/1_aBiTrlX_FBSAaht89MoL-Q.png",
            "slug": "web-gelistirme-kursu",
            "date": date(2024,9,10),
            "isActive": True
        }
    ],
    "categories": [
        {"id": 1, "name":"programlama", "slug": "programlama"},
        {"id": 2, "name":"web geliştirme", "slug": "web-gelistirme"},
        {"id": 3, "name":"mobil uygulamalar", "slug": "mobil"},
    ]
}

def index(request):
    courses = db["courses"]
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
