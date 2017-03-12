from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse

import blog
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

    return render(request, 'blog/home.html', context)

def post_detail(request, post_pk):
    """
    Recupera el detalle de un post de la base de datos
    :param request: HttpRequest
    :param post_pk: Primary Key del post a recuperar
    :return: HttpResponse
    """
    try:
        post = Post.objects.get(pk=post_pk)
    except Post.DoesNotExist:
        return HttpResponseNotFound("El post que buscas no existe.")
    except Post.MultipleObjectsReturned:
        return HttpResponse("Existen varios posts con este identificador", status=300)

    context = {
        'post': post
    }

    return render(request, 'blog/detail.html', context)