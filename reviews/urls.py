from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="index-page" ),
    path("thankyou", views.ThankYouView.as_view(), name="thankyou-page"),
    path("reviews", views.ReviewListView.as_view(), name="review-list-page"),
    path("reviews/<int:pk>/", views.DetailedView.as_view(), name="review-page")
]