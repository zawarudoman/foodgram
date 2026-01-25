from django.contrib import admin
from .models import *


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'cooking_time', 'pub_date')
    search_fields = ('name', 'author__username')
    list_filter = ('tags', 'pub_date')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)