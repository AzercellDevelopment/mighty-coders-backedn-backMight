from django.db import models


class Category(models.Model):
    """ Category Model """
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_icon = models.ImageField(null=True, blank=True, upload_to='media/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Location(models.Model):
    """Location Model"""
    location_id = models.BigAutoField(primary_key=True)
    location_name = models.CharField(max_length=100)
    location_image = models.ImageField(null=True, blank=True, upload_to='media/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.location_name


class Hotel(models.Model):
    """ Hotel Model"""
    hotel_id = models.BigAutoField(primary_key=True)
    hotel_name = models.CharField(max_length=100)
    hotel_icon_image = models.ImageField(null=True, blank=True, upload_to='media/')
    hotel_image = models.ImageField(null=True, blank=True, upload_to='media/')
    hotel_location = models.CharField(max_length=200)
    hotel_price_for_night = models.IntegerField()
    hotel_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    hotel_adress = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.hotel_name


class Meal(models.Model):
    """ Meal Model"""
    meal_id = models.BigAutoField(primary_key=True)
    meal_name = models.CharField(max_length=100)
    meal_image = models.ImageField(null=True, blank=True, upload_to='media/')
    meal_description = models.TextField()
    meal_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal_name
