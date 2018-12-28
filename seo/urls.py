from django.urls import path
from . import views

urlpatterns = [
    path('', views.seo, name='seo'),
    path('seo1', views.seo1, name='seo1')
]