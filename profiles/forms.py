from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # Render all fields except for the user field
        # since that should never change.
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        # placeholder to display on fields
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }
        # autofocus attribute on the full name
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        """we iterate through the forms fields adding a star*
        to the placeholder
           if it's a required field on the model"""

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                # 'border-black rounded-0 profile-form-input' styling in our
                # checkout/static/checkout.css
            self.fields[field].widget.attrs.update({
                'class': 'border-black rounded-0 profile-form-input'
            })

            self.fields[field].label = False
