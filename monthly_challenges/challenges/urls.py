from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("<int:month>", view=views.monthly_challenge_by_number),
    # Named Paths URLs are used to have dynamic Paths
    path("<str:month>", view=views.monthly_challenge, name="monthly-challenge"),
]
