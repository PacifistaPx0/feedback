from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect


from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from reviews.models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = "/thankyou"


"""class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = "/thankyou"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)"""
"""def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/index.html", {
            "form": form
        })
    
    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thankyou")
        
        return render(request, "reviews/index.html", {
            "form": form
        })"""


class ReviewListView(ListView):
    model = Review
    template_name = "reviews/reviews.html"
    context_object_name = 'reviews'


class DetailedView(DetailView):
    model = Review
    template_name = "reviews/single_review.html"
    context_object_name = "review"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object 
        request = self.request
        favorite_id = request.session.get("favorite_review") # safer way to access session
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context
        


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # dont store objects in session, store simple values
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)


class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data you want to pass to the template
        context['message'] = "Thank you for your review!"
        return context
