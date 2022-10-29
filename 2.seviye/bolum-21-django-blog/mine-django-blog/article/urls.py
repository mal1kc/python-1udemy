from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"

urlpatterns = [
    path('',views.articles,name="articles"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addArticle,name="addArticle"),
    path('a/<int:id>',views.detail,name="article_detail"),
    path('update/<int:id>',views.updateArticle,name="updateArticle"),
    path('delete/<int:id>',views.deleteArticle,name="deleteArticle"),
    path('addcomment/<int:id>',views.addComment,name="addComment"),
]
