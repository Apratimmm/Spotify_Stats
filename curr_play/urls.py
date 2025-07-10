from django.contrib import admin
from django.urls import path,include
from . import views as v

urlpatterns = [
        path('curr_play/',v.first,name='curr_play'),
        path('callback/',v.callback)

    ]