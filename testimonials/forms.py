from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['product', 'name', 'message']
        # Some styling for the fields
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'style': 'border: 2px solid #ced4da; border-radius: 0.25rem;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your testimonial',
                'rows': 5,
                'style': 'border: 2px solid #ced4da; border-radius: 0.25rem;'
            }),
        }
