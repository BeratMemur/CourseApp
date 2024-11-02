from django import forms
from courses.models import Course

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image')
        labels = {
            "title": "Başlık",
            "description": "Açıklama",
            "imageUrl": "Görsel-Url"
        }

        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
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


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {
            "title": "Başlık",
            "description": "Açıklama",
            "image": "Görsel-Url",
            "isActive": "Aktif mi?",
            "isHome": "Anasayfada gösterilsin mi?",
            "isUpdated": "Güncel mi?",
            "categories": "Kategoriler",
        }

        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "isActive": forms.CheckboxInput(attrs={"class":"form-check-input"}),
            "isHome": forms.CheckboxInput(attrs={"class":"form-check-input"}),
            "isUpdated": forms.CheckboxInput(attrs={"class":"form-check-input"}),
            "categories": forms.SelectMultiple(attrs={"class":"form-control"}),
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


class UploadForm(forms.Form):
    image = forms.ImageField()

