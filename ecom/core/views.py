from django.shortcuts import render
from .models import Category, Product,Vendor


def index(request):
    products=Product.objects.filter( product_status="published",featured=True,)
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

def vender_list_view(request):
    vender=Vendor.objects.all()
    return render(request,'vender_list_view.html',{'vender':vender})

def vender_detail_view(request,vid):
    vender=Vendor.objects.get(vid=vid)
    return render(request,'vender_deatil_view.html',{'vender':vender})