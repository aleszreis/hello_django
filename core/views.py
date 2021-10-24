from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, name, age):
    return HttpResponse(f'<h1>Hello {name} de {age} anos.<h1>')