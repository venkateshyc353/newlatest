from django import forms
from django.core import validators
# def validate_name(a):
#     if len(a)<5:
#         raise forms.ValidationError('please prrovide graterthan 5 charters')

class schoolform(forms.Form):
    name=forms.CharField()
    number=forms.IntegerField()
    salary=forms.FloatField()
    viage=forms.CharField()

    # def clean_name(self):
    #     inputname=self.cleaned_data['name']
    #     if len(inputname)<4:
    #         raise forms.ValidationError('please provide minimum 4 charteters')
    #     return inputname
    # def clean_number(self):
    #     inputnumber=self.cleaned_data['number']
    #     print('hai vebank clean number excuting')
    #     return  inputnumber
    #
    # def cleam_salary(self):
    #     inputsalary=self.cleaned_data['salary']
    #     if type(inputsalary)==float:
    #         # raise forms.ValidationError('please priviede float values')
    #         print('clean_salary excutinojf')
    #     return inputsalary
