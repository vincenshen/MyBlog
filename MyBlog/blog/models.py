from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="类别")

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    content = models.TextField(default=None, max_length=500, verbose_name="内容")
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title