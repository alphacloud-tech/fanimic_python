from django.shortcuts import render

# Create your views here.

def Index (request):
    
    return render(request, "fanimic/index.html")

def About (request):
    
    return render(request, "fanimic/about.html")


def Services (request):
    
    return render(request, "fanimic/services.html")

def Team (request):
    
    return render(request, "fanimic/our-team.html")

# def Contact (request):
    
#     return render(request, "fanimic/contact.html")

from django.http.response import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail, BadHeaderError #for contact form
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages       

from .forms import *                             

def Contact(request):
    
    if request.method == 'GET':
        form = ContactForm()
    else:
        
        form = ContactForm(request.POST or None)
        
        if form.is_valid():
            subject     = "Online Message"
            email       = form.cleaned_data['email']
            
            body = {
		        'name': form.cleaned_data['name'], 
		        'phone': form.cleaned_data['phone'], 
		        'message':form.cleaned_data['message'], 
		    }
		    
            message = "\n".join(body.values())
            
            try:
                # send_mail(message, email,name,phone,category, ['info@alphacloud.com.ng'])
                messages.success(request, f"Thanks {body.get('name')} for contacting us, we will get back to you")
                send_mail(subject, message, email, ['info@hgphm.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
        
    
    
    return render(request, 'fanimic/contact.html', {'form': form})


def Agriculture (request):
    
    return render(request, "fanimic/agricultural.html")


def Building (request):
    
    return render(request, "fanimic/building.html")

def Manufacturing (request):
    
    return render(request, "fanimic/manufacturing.html")

def Electrical (request):
    
    return render(request, "fanimic/electrical.html")

def Decorator (request):
    
    return render(request, "fanimic/decorator.html")

def Project (request):
    
    return render(request, "fanimic/project.html")

