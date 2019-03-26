# import json
# import requests
# url='http://127.0.0.1:8000/'
# end='api'
# r=requests.get(url+end)
# data=r.json()
# for h in data:
#     print(h)
from . models import schoolnames as s
from rest_framework import serializers

class rest(serializers.ModelSerializer):
    class Meta:
        model=s
        fields='__all__'