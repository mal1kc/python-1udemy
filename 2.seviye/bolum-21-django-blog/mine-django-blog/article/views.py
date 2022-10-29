from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .forms import ArticleForm
from .models import Article, Comment
# Create your views here.


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    return render(request,"dashboard.html",{"articles":articles})

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
    else:
        articles = Article.objects.all()
    #  for i in articles:
    #     if len(i.content) > 300:
    #         i.content = i.content[:300]
    #         # todo aklına gelirse hmtl kod içeren kısım ilk 300 deyse silmeyi dene
    
    return render(request,"articles.html",{"articles":articles})

@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,message="{} isimli makale başarıyla oluşturuldu".format(article.title))
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all()
    return render(request,"articledetail.html",{"article":article,"comments":comments})

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,message="{} isimli makale başarıyla güncellendi".format(article.title))
        return redirect("article:dashboard")
    return render(request,"articleUpdate.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,message="{} isimli makale başarıyla silindi".format(article.title))
    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        
        newComment = Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article =article
        newComment.save()
    return redirect(reverse("article:article_detail",kwargs={"id":id}))