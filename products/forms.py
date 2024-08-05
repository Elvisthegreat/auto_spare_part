from django import forms
# class imported from the widgets in our directory
from .widgets import CustomClearableFileInput
from .models import Product, Category, Testimonial


class ProductForm(forms.ModelForm):
    # Defined the model and the field we want to include
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(
            c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['message']
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
