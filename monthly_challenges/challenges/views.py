from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# The 'month' argument has to be the same as the placeholder in urls.py

challenges_dict = {
    "january": "Eat no meat for the entire month.",
    "february": "Walk for 20 minutes every day.",
    "march": "Learn Django for 45 minutes every day.",
    "april": "Sleep 8 hours a day for the entire month.",
    "may": "Eat no meat for the entire month.",
    "june": "Walk for 20 minutes every day.",
    "july": "Learn Django for 45 minutes every day.",
    "august": "Sleep 8 hours a day for the entire month.",
    "september": "Eat no meat for the entire month.",
    "october": "Walk for 20 minutes every day.",
    "november": "Learn Django for 45 minutes every day.",
    "december": None#"Sleep 8 hours a day for the entire month.",
}


def monthly_challenge_by_number(request, month: int):

    try:
        redirect_month = list(challenges_dict.keys())[month - 1]
        # Constructs '/challenges/<selected_month>'
        redirect_path = reverse("monthly-challenge", args=[redirect_month])
    except IndexError:
        return HttpResponseRedirect(f"/challenges/challenge-not-found")
    else:
        return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    if month in challenges_dict.keys():
        challenge_text = challenges_dict.get(month)
        #response_data = f"<h1>{challenge_text}</h1>"
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month#.capitalize()
        })
    else:
        raise Http404("404.html")
        response_data = render_to_string("404.html")
        #return HttpResponseNotFound("<h1>This month is incorrect or not supported yet.<h1>")
        #return HttpResponseNotFound(response_data)

def index(request):

    months = list(challenges_dict.keys())

    #response = "<ul></ul>"
    #for month in months:
    #    capitalized_month = month.capitalize()
    #    month_path = reverse("monthly-challenge", args=[month])
    #    response += f'<li><a href="{month_path}">{capitalized_month}</a></li>\n'

    #response_data = f"<ul>{response}</ul>"
    #return HttpResponse(response_data)

    return render(request, "challenges/index.html", {
        "months": months
    })