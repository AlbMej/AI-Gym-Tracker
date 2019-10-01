from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from django.core.exceptions import ValidationError
from loan_app.core.models import Loan

class LoanFieldForm(forms.ModelForm):

    class Meta:
        model = Loan
        fields = ('first_name', 'last_name', 'email', 'phone', 
                'address', 'city', 'state', 'zip_code', 'amount_required', 
                'business_type', 'years_in_business', 'other', 'agree')

        BUSINESS_TYPE = (
                ('', 'Choose...'),
                ('FT', 'Food Truck'),
                ('CON', 'Construction'),
                ('OTH', 'Other')
            )

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ex. Alberto'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ex. Mejia'}), 
            'email': forms.TextInput(attrs={'placeholder': 'Ex. me@caminofinancial.com'}), 
            'phone': forms.TextInput(attrs={'placeholder': 'Ex. 914 123 4567'}),
            'address': forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor, 1234 Main St'}),
            'city': forms.TextInput(attrs={'placeholder': 'Yonkers'}),
            'state': forms.TextInput(attrs={'placeholder': 'NY'}),
            'zip_code': forms.TextInput(attrs={'placeholder': '10701'}),
            'amount_required': forms.TextInput(attrs={'placeholder': '7500'}),
            'years_in_business': forms.TextInput(attrs={'placeholder': '3'}),
            'other': forms.TextInput(attrs={'placeholder': 'N/A'})
        }

class CustomCheckbox(Field):
    template = 'custom_checkbox.html'

class CustomFieldForm(LoanFieldForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['agree'].required = True 
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),


            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('city', css_class='form-group col-md-2 mb-0'),
                Column('state', css_class='form-group col-md-2 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('amount_required', css_class='form-group col-md-4 mb-0'),
                Column('business_type', css_class='form-group col-md-4 mb-0'),
                Column('other', css_class='form-group col-md-2 mb-0'),
                Column('years_in_business', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),

            CustomCheckbox('agree'),
            Submit('submit', 'Submit')
        )