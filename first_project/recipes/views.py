from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')


def recipe(request):
    return render(request, 'recipes/pages/home.html')
