from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout, login, authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

from .models import Category, Article


class Login(View):
    def post(self, request):
        print(request.POST)
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse("success")
        else:
            return HttpResponse("false")


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("index"))


class Register(View):
    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = User.objects.filter(username=username)
        if user:
            return HttpResponse("no")

        if password:
            User.objects.create(username=username, password=make_password(password))
            return HttpResponse("ok")


class Index(View):
    def get(self, request):
        category = Category.objects.all()
        articles = Article.objects.all().order_by("-mod_date")

        # 文章分类功能
        category_id = request.GET.get("category_id", "")
        if category_id:
            articles = articles.filter(category=category_id)

        # 文章搜索功能
        keywords = request.GET.get("keywords", "")
        if keywords:
            articles = Article.objects.filter(Q(title__icontains=keywords) |
                                              Q(content__icontains=keywords)).order_by("-mod_date")
        # 页面分页功能
        paginator = Paginator(articles, 2)
        page = request.GET.get("page", 1)
        try:
            articles = paginator.page(page)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        return render(request, "index.html", {"category": category, "articles": articles})


class ArticleCenter(View):
    def get(self, request, author_id):
        category = Category.objects.all()

        # 文章分类功能
        category_id = request.GET.get("category_id", "")
        if category_id:
            articles = Article.objects.filter(Q(author=author_id) & Q(category__id=category_id))
        else:
            articles = Article.objects.filter(author=author_id)

        # 文章搜索
        keywords = request.GET.get("keywords", "")
        if keywords:
            articles = articles.filter(Q(title__icontains=keywords) |
                                       Q(content__icontains=keywords)).order_by("-mod_date")
        return render(request, "article_center.html", {"articles": articles, "category": category})


class ArticleDetail(View):
    def get(self, request, article_id):
        category = Category.objects.all()
        article = Article.objects.get(id=article_id)
        return render(request, "article_details.html", {"article": article, "category": category})


class ArticleCreate(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, "article_create.html", {"category": category})

    def post(self, request):
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        category = request.POST.getlist("category", "")
        user = request.user.username
        author_obj = User.objects.get(username=user)
        article = Article.objects.create(title=title, content=content, author=author_obj)
        for obj in category:
            cate = Category.objects.get(id=obj)
            article.category.add(cate)
        return render(request, "article_create_success.html")


class ArticleDelete(View):
    def post(self, request):
        article_id = request.POST.get("article_id", "")
        Article.objects.filter(id=int(article_id)).delete()
        return HttpResponse("success")


class ArticleModify(View):
    def get(self, request, article_id):
        category = Category.objects.all()
        article = Article.objects.filter(id=int(article_id))[0]
        category_ids = article.category.all().values("id")
        return render(request, "article_modify.html", {
            "article": article,
            "category": category,
            "category_ids": category_ids,
        })

    def post(self, request, article_id):
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        category = request.POST.getlist("category", "")
        print(category)
        Article.objects.filter(id=article_id).update(title=title, content=content,)
        article = Article.objects.filter(id=article_id)[0]
        for obj in category:
            cate = Category.objects.get(id=obj)
            article.category.add(cate)
        return render(request, "article_modify_success.html")


class Search(View):
    pass
#     def get(self, request):
#         category = Category.objects.all()
#         keywords = request.GET.get("keywords", "")
#         article_list = Article.objects.filter(Q(title__icontains=keywords) |
#                                               Q(content__icontains=keywords)).order_by("-mod_date")
#
#         # 页面分页功能
#         paginator = Paginator(article_list, 2)
#         page = request.GET.get("page", 1)
#         try:
#             article_list = paginator.page(page)
#         except EmptyPage:
#             article_list = paginator.page(paginator.num_pages)
#         return render(request, "index.html", {"category": category, "articles": article_list})