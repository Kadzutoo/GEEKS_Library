from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('Фантастика', 'Фантастика'),
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Приключения', 'Приключения'),
        ('Драма', 'Драма'),
    ]

    title = models.CharField(max_length=200, verbose_name="Название книги")
    description = models.TextField(verbose_name="Описание книги", blank=True)
    price = models.PositiveIntegerField(verbose_name="Цена", default=500)
    release_date = models.DateField(verbose_name="Дата выхода")
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, verbose_name="Жанр")
    email = models.EmailField(verbose_name="Почта автора")
    author = models.CharField(max_length=100, verbose_name="Автор")
    image = models.ImageField(upload_to='books/', verbose_name="Обложка книги", blank=True, null=True)

    def __str__(self):
        return self.title

