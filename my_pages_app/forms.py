from django import forms
from django.forms import ModelForm
from .models import Contact


INTEREST = (
                    ("volunteering", "VOLUNTEERING"),
                    ("partnering", "PARTNERING"),
)

class ContactForm(ModelForm):
    name = forms.CharField(required=True, label = 'Full Name')
    email = forms.EmailField(required=True, label = 'Email')
    phone = forms.CharField()
    message = forms.CharField(widget= forms.Textarea(), required = True)

    class Meta:
        model = Contact
        fields = '__all__'
