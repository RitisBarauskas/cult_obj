from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SignUpForm, NewCultureObjectForm
from .models import CultureObject


def index(request):
    """
    Метод отображения главной страницы
    """
    return render(request, 'objects/index.html')


def search_objects(request):
    """
    Метод отображения формы поиска.
    """
    search_query = request.GET.get('q').split()
    if not search_query:
        return render(request, 'objects/index.html')

    query_filters = Q()
    for word in search_query:
        query_filters |= (
                Q(name__icontains=word) |
                Q(ensemble_name_on_doc__icontains=word)
        )

    objects = CultureObject.objects.filter(query_filters).distinct()

    return render(
        request,
        'objects/search_objects.html',
        {'Objects': objects},
    )


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
    objects = CultureObject.objects.all()[:10]

    return render(
        request,
        'objects/search_objects.html',
        {'Objects': objects},
    )


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
