from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ContactForm

def home(request):
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

def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

    form = ContactForm()
    context = {'form':form}
    return render(request,'contact_form.html', context)

def success(request):
    return HttpResponse("Thank you for contacting us. Your message has been sent successfully!")


#    name = data["name"]
#         email = data["email"]
#         phone = data["phone"]
#         message = data["message"]
        
#         return redirect('contact_form')