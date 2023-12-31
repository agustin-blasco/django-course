from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(View):

    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):

        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save() # This can be saved, because this is a ModelForm object.
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
            "form": form
        })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review

    context_object_name = "reviews"

    #def get_queryset(self):
    #    base_query = super().get_queryset()
    #    filtered_values = base_query.filter(rating__gt=2)
    #    return filtered_values

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    
    