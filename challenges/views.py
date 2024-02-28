from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


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

    return HttpResponse(monthly_challenges[month])


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    forward_month = months[month-1]
    return HttpResponseRedirect(f'/challenges/{forward_month}')
