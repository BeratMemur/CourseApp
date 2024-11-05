from django.contrib import admin
from pages.models import Slider

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title","course",)