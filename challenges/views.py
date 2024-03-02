from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.
from django.urls import reverse


def get_path(month):
    return reverse('monthly_challenge', args=[month])


monthly_challenges = {
    'january': "eat no meat the entire month",
    'february': "walk for at least 20 minutes every dat !",
    'march': "learn Django for at least 30 minutes every dat !",
    'april': "eat no meat the entire month",
    'may': "walk for at least 30 minutes every dat !",
    'june': "eat no meat the entire month",
    'july': "walk for at least 30 minutes every dat !",
    'august': "eat no meat the entire month",
    'september': "walk for at least 20 minutes every dat !",
    'october': "learn Django for at least 30 minutes every dat !",
    'november': "eat no meat the entire month",
    'december': "eat no meat the entire month",
}


def monthly_challenge(request, month):
    if month not in monthly_challenges.keys():
        return HttpResponseNotFound('Invalid month')
    contex = {
        'month': month,
        'challenge': monthly_challenges[month]
    }
    return render(request, 'challenges/challenge.html', contex)


def monthly_challenges_by_number(request, month):
    month_challenges = list(monthly_challenges.keys())
    forward_month = month_challenges[month - 1]
    return HttpResponseRedirect(get_path(forward_month))


def months(request):
    list_items = ""
    challenges_months = list(monthly_challenges.keys())
    for month in challenges_months:
        list_items += f'<li><a href="{get_path(month)}">{month.capitalize()}</a></li>'
    response_data = f"""
    <ul>
    {list_items}
    </ul>
    """
    return HttpResponse(response_data)
