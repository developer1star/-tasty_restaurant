from django.contrib import admin
from .models import Dish  # Make sure Dish is defined in models.py

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
