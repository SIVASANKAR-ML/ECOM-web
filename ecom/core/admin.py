from django.contrib import admin
from .models import Vendor, Category, Product, ProductImages, CartOrder, CartOrderItem,ProductReview,WishList,Address

# Register your models here
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'contact', 'shipping_time', 'authenticate_rating', 'day_return', 'warranty')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'old_price','image','product_status', 'sku', 'date')

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'date')

@admin.register(CartOrder)
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'paid_status', 'order_status', 'product_status')

@admin.register(CartOrderItem)
class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'qty', 'price', 'total','paid_status')

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display=('user','product','review','rating','date')

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display=('user','product','date')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display=('user','address','status')

