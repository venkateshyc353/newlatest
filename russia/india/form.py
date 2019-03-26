from django import forms

class studentfrom(forms.Form):
    name=forms.CharField()
    number=forms.IntegerField()