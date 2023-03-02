from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse('<h1>This is Home!</h1>')

def about_view(request):
    return HttpResponse('<h1>This is About!</h1>')

def contact_view(request):
    return HttpResponse('<h1>This is Contact!</h1>')