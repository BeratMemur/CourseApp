from django.contrib import admin
from .models import Course, Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "isActive", "isHome", "isUpdated", "category_list",)
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("isUpdated", "isActive", "isHome",)
    list_editable = ("isActive", "isUpdated", "isHome",)
    search_fields = ("title", "description",)

    def category_list(self, course):
        list = ""
        for category in course.categories.all():
            list += category.name + " / "
        return list


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "course_count")
    prepopulated_fields = {"slug": ("name",),}

    def course_count(self, category):
        return category.course_set.count()