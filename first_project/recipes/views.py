from django.shortcuts import render

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def recipe(request, id):
    recipe = Recipe.objects.get(pk=id)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes
    })
