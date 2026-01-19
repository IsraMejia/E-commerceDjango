from django import forms 
from . models import ShippingAddress

class ShippingForm(forms.ModelForm):
    
    class Meta:
        model = ShippingAddress
        fileds = ['full_name', 'email', 'address1', 'address2', 'city', 'state', 'zipcode'] 
        exclude = ['user',] #ForeingKey