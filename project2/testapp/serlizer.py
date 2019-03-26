from rest_framework import serializers
from .models import schoolmodel
class api(serializers.ModelSerializer):
    class Meta:
        model=schoolmodel
        fields='__all__'