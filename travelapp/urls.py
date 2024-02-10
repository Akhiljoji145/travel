from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.main,name='main'),
    path('register/',views.user_reg,name='register'),
    path('login/',views.login,name='login'),
    path('userlogin/',views.user_login,name='userlogin'),
]