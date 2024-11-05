from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", blank=True, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.name}"
    

class Course(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, default="")
    description = RichTextField()
    image = models.ImageField(upload_to="images", default="")
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    isUpdated = models.BooleanField(default=True)
    slug = models.SlugField(default="", blank=True, unique=True, db_index=True)
    categories = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.title}"
    

class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")
