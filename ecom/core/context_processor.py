from .models import Vendor, Category, Product, ProductImages, CartOrder, CartOrderItem,ProductReview,WishList,Address

def default(request):
    categories=Category.objects.all()
    return{
        'categories':categories
    }