from django import forms
from django.utils.translation import ugettext as _
from django.conf import settings

class BMICalculateForm(forms.Form):
    weight = forms.FloatField()
    height = forms.FloatField(help_text=_('height in centimeters. use 170 if you own 1.70 meters.'))

    def calculate(self):
        bmi = ''
        if 'weight' in self.cleaned_data and 'height' in self.cleaned_data:
            bmi = self.cleaned_data['weight'] / (self.cleaned_data['height'] ** 2)
        return bmi
