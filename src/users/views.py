from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect


def login(request):

    context = dict()
    if request.method == "POST":
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