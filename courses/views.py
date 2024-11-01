from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, Category
from django.core.paginator import Paginator


def index(request):
    courses = Course.objects.filter(isActive=1, isHome=1)
    categories = Category.objects.all()

    return render(request, 'courses/index.html', {
        'courses': courses,
        'categories': categories
    })

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        courses = Course.objects.filter(isActive=1, title__contains=q).order_by("date")
        categories = Category.objects.all()
    else:
        return redirect("/courses")
    
    return render(request, "courses/search.html", {
        'courses': courses,
        'categories': categories,
    })


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    return render(request, 'courses/details.html',context)


def getCoursesByCategory(request, slug):
    courses = Course.objects.filter(categories__slug = slug, isActive=1).order_by("date")
    categories = Category.objects.all()

    paginator = Paginator(courses, 3)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, "courses/list.html", {
        'page_obj': page_obj,
        'categories': categories,
        'activeCategory': slug
    })
    