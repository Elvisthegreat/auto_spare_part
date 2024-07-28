from django import forms
from .models import ContactRequest

class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contact-us'}),
            'email': forms.EmailInput(attrs={'class': 'contact-us'}),
            'message': forms.Textarea(attrs={'class': 'contact-us'}),
        }
