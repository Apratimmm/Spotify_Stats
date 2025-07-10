from django.contrib import admin
from django.urls import path,include
from . import views as v

urlpatterns = [
        path('',v.first,name='top_artists'),
        path('callback/',v.callback)
    ]