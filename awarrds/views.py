from django.shortcuts import render
from django.http import HttpResponse


# Creating views
def index(request):
    return HttpResponse('Welcome to the Award-site')