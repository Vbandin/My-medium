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

    if request.GET.get('filter') == 'authored':
        posts = posts.filter(author=request.user)

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

def authors_list(request):
    """
    Recupera todos los blogs de la base de datos y los pinta
    :param request: HttpRequest
    :return: HttpResponse
    """
    authors = Post.objects.select_related("author").all()
    posts = posts.filter(author=request.user)
    context = {
        'authors_objects': author
    }

    return render(request, 'blog/blogs.html', context)

def author_posts(request, author_id):
    """
    Recupera de la base de datos todos los posts del mismo autor
    :param request: HttpRequest
    :param author: Identifica al autor para recuperar sus posts
    :return: HttpResponse
    """
    try:
        author = Post.objects.get(author=author_id)
    except Post.author.DoesNotExist:
        return HttpResponseNotFound("El autor que buscas aún no ha escrito nada.")
    except Post.MultipleObjectsReturned:
        return HttpResponse("Existen varios autores con este identificador", status=300)

    context = {
        'author_posts': author
    }

    return render(request, 'blog/author.html', context)