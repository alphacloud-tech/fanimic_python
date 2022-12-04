from django import forms
from django.core.mail import message
from django.forms.widgets import Textarea


class ContactForm (forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    number = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['placeholder'] = 'name'
        self.fields['name'].widget.attrs['class'] = 'form-control  border border-danger' 
        
        self.fields['email'].widget.attrs['placeholder'] = 'last name'
        self.fields['email'].widget.attrs['class'] = 'form-control  border border-danger' 
        
        self.fields['number'].widget.attrs['placeholder'] = 'Enter Your Number'
        self.fields['number'].widget.attrs['class'] = 'form-control  border border-danger' 
        
        self.fields['message'].widget.attrs['placeholder'] = 'Enter your message'
        self.fields['message'].widget.attrs['class'] = 'form-control  border border-danger' 

