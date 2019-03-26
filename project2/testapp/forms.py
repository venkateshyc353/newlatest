from django import forms
from .models import  schoolmodel as s
class schoolform(forms.ModelForm):
    class Meta:
        model=s
        fields='__all__'