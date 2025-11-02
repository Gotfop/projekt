from django import forms
from .models import Oder


class OderForm(forms.ModelForm):
     
     class Meta:
        model = Oder
        fields = ['number_order','client_id','tomats']
        widgets = {'tomats': forms.CheckboxSelectMultiple}

