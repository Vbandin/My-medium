from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post


def posts_list(request):
    """
    Recupera todos los post de la base de datos y los pinta
    :param request: HttpRequest
    :return: HttpResponse
    """
    posts = Post.objects.all()

    context = {
        'post_objects': posts
    }

    return render(request, 'blog/home.html')