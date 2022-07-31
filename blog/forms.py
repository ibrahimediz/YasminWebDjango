from pyexpat import model
from django.forms import ModelForm
from .models import BlogModel

class BlogForm(ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title','content']