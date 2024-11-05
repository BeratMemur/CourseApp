from django.db import models
from courses.models import Course

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    isActive = models.BooleanField(default=False)
    course = models.OneToOneField(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"