from django.urls import path
from userauth import views

app_name='sign-up'

urlpatterns = [
    path('sign-up/',views.registerUser, name='sign-up'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),
]
