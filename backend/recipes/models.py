from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tag(models.Model):
    name = models.CharField('Название', max_length=200, unique=True)
    slug = models.SlugField('Slug', max_length=200, unique=True)

class Ingredient(models.Model):
    name = models.CharField('Название', max_length=200)
    measurement_unit = models.CharField('Единица измерения', max_length=200)

class Recipe(models.Model):
    name = models.CharField('Название', max_length=200)
    text = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='recipes/')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    tags = models.ManyToManyField(Tag, related_name='recipes')
    cooking_time = models.PositiveIntegerField('Время приготовления')
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
