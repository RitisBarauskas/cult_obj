from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import *
# from .forms import SignUpForm
from .models import *


def index(request):
    return render(request, 'objects/index.html' )

def index2(request):
    return render(request, 'objects/index2.html')


class HomePageView(TemplateView):
    template_name = 'index.html'


class SearchResultsView(ListView):
    model = CultureObject
    template_name = 'index2.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = CultureObject.objects.filter(
            Q(Name__icontains=query) | Q(Type__icontains=query)
        )
        return object_list


@login_required
def add(request):
    if request.method == 'POST':
       form = CultureObject(request.POST)
       form.save()
       return redirect('index')


    form = NewCultureObjectForm()
    context = {
        'form': form
    }
    return render(request, 'objects/add.html', context)

def profile(request):
    return render(request, 'objects/profile.html')

def show(request):
    culture = CultureObject.objects.all()
    return render(request,"index2.html",{'Objects':culture})


def rg(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/rg.html', {'form': form})





