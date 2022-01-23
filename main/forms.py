from django.forms import ModelForm
from .models import (
    Location,
    Category,
    Hotel,
    Meal,
)


class LocationForm(ModelForm):

    class Meta:
        model = Location

        fields = ['location_name', 'location_image', 'categories']


class CategoryForm(ModelForm):

    class Meta:
        model = Category

        fields = ['category_name', 'category_icon']


class HotelForm(ModelForm):

    class Meta:
        model = Hotel

        fields = ['hotel_name', 'hotel_image', 'hotel_icon_image', 'hotel_location', 'hotel_price_for_night', 'hotel_adress' ]


class MealForm(ModelForm):

    class Meta:
        model = Meal

        fields = ['meal_name', 'meal_image', 'meal_description', 'meal_location']
