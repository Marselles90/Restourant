from django.shortcuts import render
from .models import Food, BookTable, Table, Response, Event, Category


def home(request):
    return render(request, 'home.html')


def menu_category(request, id):
    menu_category = Category.objects.get(id=id)
    context = {
        'menu_category': menu_category,
    }
    return render(request, 'menu.html', 'context')


def menu(request):
    categories = Category.objects.all()
    foods = Food.objects.all()
    context = {
        'categories': categories,
        'foods': foods,
    }
    return render(request, 'menu.html', context)


def booktable(request):
    tables = BookTable.objects.all()
    return render(request, 'booktable.html', {'tables': tables})


def contact(request):
    return render(request, 'contact.html')


def event(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'event.html', context)