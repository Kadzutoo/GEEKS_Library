from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from. models import Book



def book_list(request):
    if request.method == 'GET':
        book_list = models.Book.objects.all().order_by('-release_date')
        context = {'book_list': book_list}
        return render(request, template_name='book_list', context=context)



def book_detail(request, id):
    if request.method == 'GET':
        book = get_object_or_404(models.Book, id=id)
        context = {'book': book}
        return render(request, template_name='book_detail', context=context)


# about_me
def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Привет! Я Арген, студент IT-Академии Geeks")

# about_my_pets
def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse("У меня есть кот по имени Мура (Муракан) и ему 3 года.")

# Текущее время
def date_time(request):
    if request.method == 'GET':
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Текущее время: {formatted_time} ")
