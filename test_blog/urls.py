"""test_blog URL Configuration

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
from article import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home,name="home"),
    url(r'^title_(?P<title>.*)$',views.article_detail,name="article_detail"),
    url(r'^category_(?P<category>\w+)$',views.article_category,name="article_category"),
    url(r'^test/$',views.test,name="test"),
    url(r'^search/$',views.article_search,name='article_search'),
    url(r'^guidang/$',views.guidang,name='guidang'),

]
