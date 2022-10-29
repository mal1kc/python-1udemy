from django import forms
from django.db.models.base import Model
from django.forms.models import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content',"article_image"]
