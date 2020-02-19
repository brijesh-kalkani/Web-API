from django.contrib import admin
from django.urls import path,include
# from rest_framework.urlpatterns import format_suffix_pattern
from . import views
urlpatterns = [
    path('',views.PersonView.as_view()),
]
