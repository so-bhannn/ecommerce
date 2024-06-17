from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'services/index.html')

def home(request):
    return render(request, 'services/home.html')

def shoppingcart(request):
    return render(request,'services/shopppingcart.html')

def checkout(request):
    pass
