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

from blog.views import posts_list, post_detail, NewPostView, author_blog, blogs_view
from users.views import LoginView, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', posts_list, name="posts_list"),
    url(r'^blogs/username/(?P<post_pk>[0-9]+)$', post_detail, name="post_detail"),
    url(r'^blogs/new-post$', NewPostView.as_view(), name="new_post"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^blogs/(?P<username>[-\w]+)/$', author_blog, name="author_blog"),
    url(r'^blogs$', blogs_view, name="blogs_view")
]
