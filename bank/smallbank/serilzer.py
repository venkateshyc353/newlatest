from rest_framework import serializers
from .models import person

class restapiselizer(serializers.ModelSerializer):
    class Meta:
        model=person
        fields=('firstname','lastname')