from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewCultureObjectForm, SignUpForm
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
    search_query = request.GET.get('q')
    if not search_query:
        return render(request, 'objects/index.html')

    query_filters = Q()
    for word in search_query.split():
        query_filters |= (
                Q(name__icontains=word) |
                Q(ensemble_name_on_doc__icontains=word)
        )

    objects = CultureObject.objects.filter(query_filters).distinct()
    if not objects.exists():
        return render(
            request,
            'objects/search_objects.html',
            {'not_found': True},
        )

    display_obj = objects.count() // 15
    if display_obj < 10:
        display_obj = 10
    paginator = Paginator(objects, display_obj)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(
        request,
        'objects/search_objects.html',
        {"page": page, "paginator": paginator},
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
    objects = CultureObject.objects.all()
    display_obj = objects.count() // 15
    paginator = Paginator(objects, display_obj)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(
        request,
        'objects/search_objects.html',
        {"page": page, "paginator": paginator},
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
