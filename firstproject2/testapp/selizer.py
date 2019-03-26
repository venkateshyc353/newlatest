from rest_framework import serializers
from .models import schoolapp

class webapi(serializers.ModelSerializer):
    class Meta:
        model=schoolapp
        fields='__all__'