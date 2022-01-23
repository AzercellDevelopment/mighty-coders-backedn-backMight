from django.shortcuts import render
from django.views import View
from .models import (
    Location,
    Hotel,
    Meal,
    Category,
)


def main_page(request):
    context = {
        "locations": Location.objects.all(),
        "hotels": Hotel.objects.all(),
        "meals": Meal.objects.all(),
        "categories": Category.objects.all()
    }
    return render(request, 'index.html', context)
