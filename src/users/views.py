from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import request
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm


class LoginView(View):

    def get(self, request):
        """
        Presenta el formulario de login a un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        context = {
            'form': LoginForm()
        }
        return render(request, 'login.html', context)


    def post(self, request):
        """
        Hace login de un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = LoginForm(request.POST)
        context = dict()
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                request.session["default-language"] = "es"
                django_login(request, user)
                url = request.GET.get('next', 'posts_list')
                return redirect(url)
            else:
                context["error"] = "Wrong username or password"
        context["form"] = form
        return render(request, 'login.html', context)

def logout(request):
    django_logout(request)
    return redirect('login')