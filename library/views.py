from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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
        return HttpResponse(f"Текущее время: {formatted_time} 🕒")
