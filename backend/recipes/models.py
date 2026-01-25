from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Recipe(models.Model):
    name = models.CharField('Название', max_length=200)
    text = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='recipes/')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
