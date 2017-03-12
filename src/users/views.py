from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import request
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):

    def get(self, request):
        """
        Presenta el formulario de login a un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        context = dict()
        return render(request, 'login.html', context)


    def post(self, request):
        """
        Hace login de un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        context = dict()
        username = request.POST.get("usr")
        password = request.POST.get("pwd")
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session["default-language"] = "es"
            django_login(request, user)
            url = request.GET.get('next', 'posts_list')
            return redirect(url)
        else:
            context["error"] = "Wrong username or password"
        return render(request, 'login.html', context)

def logout(request):
    django_logout(request)
    return redirect('login')