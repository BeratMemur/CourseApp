from django.urls import path
from.import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.details, name="details_page"),
    path('category/<slug:slug>', views.getCoursesByCategory, name='courses_by_category'),
]
