from django.urls import path
from . import views

urlpatterns = [
    path('admin_login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path('locations/', views.locations, name='locations'),
    path('locations/create/', views.locations_create, name='locations_create'),
    path('locations/edit/<int:location_id>', views.locations_edit, name='locations_edit'),
    path('locations/delete/<int:location_id>', views.locations_delete, name='locations_delete'),

    path('categories/', views.categories, name='categories'),
    path('categories/create/', views.categories_create, name='categories_create'),
    path('categories/edit/<int:category_id>', views.categories_edit, name='categories_edit'),
    path('categories/delete/<int:category_id>', views.categories_delete, name='categories_delete'),

    path('hotels/', views.hotels, name='hotels'),
    path('hotels/create/', views.hotels_create, name="hotels_create"),
    path('hotels/edit/<int:hotel_id>', views.hotels_edit, name="hotels_edit"),
    path('hotels/delete/<int:hotel_id>', views.hotels_delete, name="hotels_delete"),

    path('meals/', views.meals, name='meals'),
    path('meals/create/', views.meals_create, name='meals_create'),
    path('meals/edit/<int:meal_id>', views.meals_edit, name='meals_edit'),
    path('meals/delete/<int:meal_id>', views.meals_delete, name='meals_delete'),
]
