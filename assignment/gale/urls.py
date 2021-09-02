from django.contrib import admin
from django.urls import path
from gale.views import Index

urlpatterns = [
    path('gale/', Index.as_view(), name="index"),
]
