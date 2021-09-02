from django.contrib import admin
from django.urls import path
from website.views import Index

urlpatterns = [
    path('', Index.as_view(), name="index"),
]
