from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="yazar")
    title = models.CharField(max_length=50, verbose_name="başlık")
    content = RichTextField()
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="oluşturma tarihi")
    article_image = models.ImageField(
        blank=True, null=True, verbose_name="makale fotoğrafı")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="isim")
    comment_content = models.CharField(max_length=300, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+"," + str(self.comment_author)

    class Meta:
        ordering = ['-comment_date']

# Create your models here.
