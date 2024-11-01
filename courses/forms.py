from django.forms import ModelForm, SelectMultiple, TextInput, Textarea, CheckboxInput
from courses.models import Course

class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'imageUrl')
        labels = {
            "title": "Başlık",
            "description": "Açıklama",
            "imageUrl": "Görsel-Url"
        }

        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "imageUrl": TextInput(attrs={"class":"form-control"}),
        }

        error_messages = {
            "title": {
                "required": "Başlık alanı boş olamaz.",
                "max_lenght": "En fazla 50 karakter girilebilir."
            },
            "description": {
                "required": "Açıklama alanı boş olamaz."
            }
        }


class CourseEditForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {
            "title": "Başlık",
            "description": "Açıklama",
            "imageUrl": "Görsel-Url",
            "isActive": "Aktif mi?",
            "isHome": "Anasayfada gösterilsin mi?",
            "isUpdated": "Güncel mi?",
            "categories": "Kategoriler",
        }

        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "imageUrl": TextInput(attrs={"class":"form-control"}),
            "isActive": CheckboxInput(attrs={"class":"form-check-input"}),
            "isHome": CheckboxInput(attrs={"class":"form-check-input"}),
            "isUpdated": CheckboxInput(attrs={"class":"form-check-input"}),
            "categories": SelectMultiple(attrs={"class":"form-control"}),
        }

        error_messages = {
            "title": {
                "required": "Başlık alanı boş olamaz.",
                "max_lenght": "En fazla 50 karakter girilebilir."
            },
            "description": {
                "required": "Açıklama alanı boş olamaz."
            }
        }