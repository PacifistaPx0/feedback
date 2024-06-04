from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="index-page" ),
    path("thankyou", views.thankyou, name="thankyou-page")
]