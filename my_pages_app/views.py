from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())
    return render(request, 'home.html', {})

def who_we_are(request):
    return render(request, 'who_we_are.html', {})

def programs(request):
    return render(request, 'programs.html', {})

def make_an_impact(request):
    return render(request, 'make_an_impact.html', {})

def get_in_touch(request):
    return render(request, 'get_in_touch.html', {})

def donate(request):
    return render(request, 'donate.html', {})
