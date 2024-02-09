from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.main,name='main'),
    path('news/',views.news,name='news'),
    path('contact/',views.contact,name='contact')
]