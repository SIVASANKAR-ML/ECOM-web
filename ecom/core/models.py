from django.db import models
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField
from userauth.models import User


STATUS_CHOICE = (
    ("process", "Processing"),
    ("shipped", 'Shipped'),
    ("delivered", "Delivered"),
)

STATUS = (
    ("draft", "Draft"),
    ("disabled", 'Disabled'),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)

RATING = (
    ("1", "⭐"),
    ("2", '⭐⭐'),
    ("3", "⭐⭐⭐"),
    ("4", "⭐⭐⭐⭐"),
    ("5", "⭐⭐⭐⭐⭐"),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)#to save images in the file automaticaly 


class Category(models.Model):
    cid = ShortUUIDField(unique=True, max_length=30, prefix='cat', alphabet='abcdefghi1123456')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


# class Tags(models.Model):
#     pass


class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, max_length=30, prefix='ven', alphabet='abcdefghi1123456')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(null=True, blank=True)

    address = models.CharField(max_length=100, default='lfc road kaloor kerala')
    contact = models.CharField(max_length=100, default='12345678')
    chat_resp_time = models.CharField(max_length=100, default='100')
    shipping_time = models.CharField(max_length=100, default='100')
    authenticate_rating = models.CharField(max_length=100, default='100')
    day_return = models.CharField(max_length=100, default='100')
    warranty = models.CharField(max_length=100, default='100')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Product(models.Model):
    pid = ShortUUIDField(unique=True, max_length=30, alphabet='abcdefghi1123456')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(null=True, blank=True, default='this is a product')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category,related_name='products', on_delete=models.SET_NULL, null=True)#using related name is a good practies for showing total no of products in each category
    Vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default='599')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default='499')

    specification = models.TextField(null=True, blank=True, default='this is a product')
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    product_status = models.CharField(choices=STATUS, max_length=10, default='in_review')

    status=models.BooleanField(default=True)
    in_stock=models.BooleanField(default=True)
    featured=models.BooleanField(default=False)
    digital=models.BooleanField(default=False)
    
    sku = ShortUUIDField(unique=True, max_length=30, alphabet='abcdefghi1123456')

    date = models.DateField(auto_now_add=True)
    update = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price


class ProductImages(models.Model):
    image = models.ImageField(upload_to='product-images')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product images"


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid_status = models.BooleanField(default=False)
    order_status = models.BooleanField(default=False)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default='processing')

    class Meta:
        verbose_name_plural = "Cart orders"


class CartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    paid_status = models.CharField(max_length=300)
    item = models.CharField(max_length=300)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Cart order items"

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    review=models.TextField()
    rating=models.IntegerField(choices=RATING,default='null')
    date=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "product review"
    
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.product.title
    def get_rating(self):
        return self.rating


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    date=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "wish list"
    
    def __str__(self):
        return self.product.title

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address=models.CharField(max_length=300,null=True)
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Address"
