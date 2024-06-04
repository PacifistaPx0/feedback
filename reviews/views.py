from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect


from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .forms import ReviewForm
from reviews.models import Review

# Create your views here.


class ReviewView(View):
    def get(self, request):
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
        })
    
class ReviewListView(ListView):
    model = Review
    template_name = "reviews/reviews.html"
    context_object_name = 'reviews'

class DetailedView(DetailView):
    model = Review
    template_name = "reviews/single_review.html"
    context_object_name = "review"
    


class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data you want to pass to the template
        context['message'] = "Thank you for your review!"
        return context

