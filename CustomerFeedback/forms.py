from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import CustomerFeedback

class CustomerFeedbackForm(ModelForm):
    class Meta:
        model = CustomerFeedback
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Please enter your Full Name'}),
            'email': forms.TextInput(attrs={'placeholder':'Please enter your Email Address'}),
            'phone_No': forms.TextInput(attrs={'placeholder':'Please enter your Phone Number'}),
            'comments': forms.Textarea(attrs={'placeholder':'Please enter your Comments','rows':4, 'cols':15})
        }
        fields = '__all__'