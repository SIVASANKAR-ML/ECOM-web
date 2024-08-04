from django.urls import include, path
from core import views
from django.conf import settings
from django.conf.urls.static import static

app_name='index'

urlpatterns = [
    path('',views.index,name='index'),
    path("product/",views.product_list,name='product-list'),
    path("category/",views.category_list, name="category-list"),
    path("category/<cid>/",views.category_list_view, name="category-list-view")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)