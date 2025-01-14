from django.contrib import admin
from . import models
from .models import Book



admin.site.register(models.Book)  # Регистрация модели Book
