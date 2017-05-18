"""MyBBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import Index, ArticleCreate, ArticleDetail, Login, Logout, ArticleCenter, ArticleDelete, ArticleModify, Register, Search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", Index.as_view(), name="index"),
    url(r"^detail/(?P<article_id>\d+)/$", ArticleDetail.as_view(), name="detail"),
    url(r"^create/$", ArticleCreate.as_view(), name="create_article"),
    url(r"^login/$", Login.as_view(), name="login"),
    url(r"^logout/$", Logout.as_view(), name="logout"),
    url(r"^register/$", Register.as_view(), name="register"),
    url(r"^article_center/(?P<author_id>\d+)/$", ArticleCenter.as_view(), name="article_center"),
    url(r"^article_delete/$", ArticleDelete.as_view(), name="article_delete"),
    url(r"^article_modify/(?P<article_id>\d+)/$", ArticleModify.as_view(), name="article_modify"),
    url(r"^search/$", Search.as_view(), name="search")
]
