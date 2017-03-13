from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

import blog
from blog.forms import PostForm
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
        return render(request, '404.html', {}, status=404)
    except Post.MultipleObjectsReturned:
        return HttpResponse("Existen varios posts con este identificador", status=300)

    context = {
        'post': post
    }

    return render(request, 'blog/detail.html', context)

class NewPostView(View):

    @method_decorator(login_required)
    def get(self, request):
        # crear el formulario
        form = PostForm()

        # renderiza la plantilla con el formulario
        context = {
            "form": form
        }
        return render(request, 'blog/new.html', context)

    @method_decorator(login_required)
    def post(self, request):
        # crear el formulario con los datos del POST
        post_with_user = Post(author=request.user)
        form = PostForm(request.POST, instance=post_with_user)

        # validar el formulario
        if form.is_valid():
            # crear la tarea
            post = form.save()

            # mostrar mensaje de exito
            message = 'Tarea creada con éxito! <a href="{0}">Ver tarea</a>'.format(
                reverse('post_detail', args=[post.pk])  # genera la URL de detalle de esta tarea
            )

            # limpiamos el formulario creando uno vacío para pasar a la plantilla
            form = PostForm()
        else:
            # mostrar mensaje de error
            message = "Se ha producido un error"

        # renderizar la plantilla
        context = {
            "form": form,
            "message": message
        }
        return render(request, 'blog/new.html', context)

def author_blog(request, username):
    """
    Creo las urls de perfil de usuario/blog
    :param request: HttpRequest
    :param username: username del propietario del blog
    :param author: recupera el autor de la base de datos para filtrar los posts
    :return: HttpResponse
    """
    u = User.objects.get(username=username)
    posts = Post.objects.all()
    context = {
        'user_blog': u,
        'post_objects': posts
    }
    return render(request, 'blog/author.html', context)

def blogs_view(request, author):
    """
    Creo las urls de perfil de usuario/blog
    :param request: HttpRequest
    :param author: recupera el autor para mostrar los blogs
    :return: HttpResponse
    """
    author = Post.objects.get(author=author)

    context = {
        'user_blogs': author
    }
    return render(request, 'blog/blogs.html', context)