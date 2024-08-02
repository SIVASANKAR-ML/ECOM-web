from django.urls import include, path
from core import views
from django.conf import settings
from django.conf.urls.static import static

app_name='index'

urlpatterns = [
    path('',views.index,name='index')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)