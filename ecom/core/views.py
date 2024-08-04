from django.shortcuts import render
from .models import Category, Product


def index(request):
    products=Product.objects.filter( product_status="published",featured=True)
    return render(request,'index.html',{'products':products})

def product_list(request):
    products=Product.objects.filter(featured=True)
    return render(request,'product-list.html',{'products':products})

def category_list(request):
    categories = Category.objects.all()
    for category in categories:
        category.count = category.products.count()  # 'products' is the related name for the reverse relation
    return render(request, 'category-list.html', {'categories': categories})

def category_list_view(request,cid):
    category=Category.objects.get(cid=cid)
    products=Product.objects.filter( product_status="published",category=category)
    return render(request,'category-list-view.html',{'category':category,'products':products})
