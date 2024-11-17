from django.shortcuts import get_object_or_404, render
from .models import Category, Product,Vendor
from taggit.models import Tag


def index(request):
    products=Product.objects.filter( product_status="published",featured=True,).select_related('vender')
    return render(request,'base.html',{'products':products})

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
    products=Product.objects.filter(product_status="published",vender=vender)#'vender'is from models product.vender
    return render(request,'vender_deatil_view.html',{'vender':vender,'products':products})

def product_detail_view(request,pid,vid):
    vender=Vendor.objects.get(vid=vid)
    products=Product.objects.get(pid=pid)
    cproduct=Product.objects.filter(category=products.category).exclude(pid=pid) # exclude: this is used to remove current viewed product from the related product 
    p_image=products.p_images.all()
    return render(request,'product_detail_view.html',{'products':products,'vender':vender,'p_image':p_image,'cproduct':cproduct})

def tag_list(request,tag_slug=None):
    products=Product.objects.filter(product_status="published")

    tags=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        products=Product.objects.filter(tags__in=[tag])

    return render(request,'tag_list.html',{'products':products,'tags':tags})