from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SignUpForm, NewCultureObjectForm
from .models import CultureObject


def index(request):
    """
    Метод отображения главной страницы
    """
    return render(request, 'objects/index.html' )


def search_objects(request):
    """
    Метод отображения формы поиска.
    """
    return render(request, 'objects/index.html' )


@login_required
def add(request):
    """
    Добавляет новый объект культурного наследия.
    """
    form = NewCultureObjectForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('index')

    context = {'form': form}

    return render(request, 'objects/add.html', context)


def profile(request):
    """
    Отображает профиль пользователя.
    """
    return render(request, 'objects/profile.html')


def show(request):
    """
    Показывает все объекты культурного наследия.
    """
    culture = CultureObject.objects.all()
    return render(request,"search_objects.html",{'Objects':culture})


def rg(request):
    """
    Форма и метод регистрации новых пользователей на сайте.
    """
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('index')

    return render(request, 'registration/rg.html', {'form': form})





