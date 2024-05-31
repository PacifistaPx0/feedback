from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index-page" ),
    path("thankyou", views.thankyou, name="thankyou-page")
]