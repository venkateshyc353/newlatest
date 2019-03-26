from django import forms
from django.core import validators
def name(val):
    if val<5:
        raise forms.ValidationError('pleas length')
    return val

class schoolform(forms.Form):
    name=forms.CharField()
    number=forms.IntegerField()
    feedback=forms.CharField()
    salary=forms.FloatField()


    def clean(self):
        print('this total sof cleaing in single')
        toatl_clean_data=super().clean()
        inputname=toatl_clean_data['name']
        if inputname[0] != 'v':
            raise forms.ValidationError('please provide stats with v')
        inputnumber=toatl_clean_data['number']
        if inputnumber<100:
            raise forms.ValidationError('please correct')