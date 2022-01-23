from django.shortcuts import render, redirect
from .models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from main.models import (
    Location,
    Category,
    Hotel,
    Meal,
)
from main.forms import (
    LocationForm,
    CategoryForm,
    HotelForm,
    MealForm,
)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(email=email).first()
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {"form": form})


@login_required
def dashboard(request):
    return render(request, 'adminstrator/index.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def locations(request):

    context = {
        "locations":  Location.objects.all(),
        "title": "Locations"
    }
    return render(request, 'locations/locations.html', context)


@login_required
def locations_create(request):
    if request.method == "POST":
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("locations")
    else:
        form = LocationForm()
    return render(request, 'locations/locations_create.html', {'form': form})


@login_required
def locations_edit(request, location_id):
    location = get_object_or_404(Location, pk=location_id)

    if request.method == "POST":
        form = LocationForm(request.POST, request.FILES, instance=location)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            return redirect("locations")
    else:
        form = LocationForm(instance=location)
    return render(request, 'locations/locations_edit.html', {'form': form})


@login_required
def locations_delete(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    location.delete()
    return redirect('locations')


@login_required
def categories(request):
    context = {
        "categories": Category.objects.all(),
        "title": "Category"
    }
    return render(request, 'categories/categories.html', context)


@login_required
def categories_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm()
    return render(request, 'categories/categories_create.html', {'form': form})


@login_required
def categories_edit(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect("categories")
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/categories_edit.html', {'form': form})


@login_required
def categories_delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect('categories')


@login_required
def hotels(request):
    context = {
        "hotels": Hotel.objects.all(),
        "title": "Hotel"
    }
    return render(request, 'hotels/hotels.html', context)


@login_required
def hotels_create(request):
    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("hotels")
    else:
        form = HotelForm()
    return render(request, 'hotels/hotels_create.html', {'form': form})


@login_required
def hotels_edit(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)

    if request.method == "POST":
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.save()
            return redirect("hotels")
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'hotels/hotels_edit.html', {'form': form})


@login_required
def hotels_delete(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    hotel.delete()
    return redirect('hotels')


@login_required
def meals(request):
    context = {
        "meals": Meal.objects.all(),
        "title": "Meals"
    }
    return render(request, 'meals/meals.html', context)


@login_required
def meals_create(request):
    if request.method == "POST":
        form = MealForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("meals")
    else:
        form = MealForm()
    return render(request, 'meals/meals_create.html', {'form': form})


@login_required
def meals_edit(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)

    if request.method == "POST":
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.save()
            return redirect("meals")
    else:
        form = MealForm(instance=meal)
    return render(request, 'meals/meals_edit.html', {'form': form})


@login_required
def meals_delete(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    meal.delete()
    return redirect('meals')
