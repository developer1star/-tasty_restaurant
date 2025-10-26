from django.shortcuts import render
from .models import Dish  # Make sure your model is Dish

def menu_list(request):
    dishes = Dish.objects.all()  # fetch all dishes
    return render(request, "menu/food_list.html", {"dishes": dishes})
