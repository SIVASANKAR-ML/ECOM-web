from django.shortcuts import render
from .models import Category, Product


def index(request):
    products=Product.objects.filter( product_status="published",featured=True)
    return render(request,'index.html',{'products':products})

def product_list(request):
    products=Product.objects.filter(featured=True)
    return render(request,'product-list.html',{'products':products})

def category_list(request):
    category=Category.objects.all()
    return render(request,'category-list.html',{'category':category})