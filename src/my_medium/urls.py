"""my_medium URL Configuration

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

from blog.views import posts_list, post_detail, author_posts, authors_list
from users.views import LoginView, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', posts_list, name="posts_list"),
    url(r'^post/(?P<post_pk>[0-9]+)$', post_detail, name="post_detail"),
    url(r'^blogs/', authors_list, name="authors_list"),
    url(r'^author/', author_posts, name="post_author"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', logout, name="logout")
]
