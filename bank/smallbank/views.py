from django.shortcuts import render
from . models import person
from .serilzer import  restapiselizer
import json

from django.http import JsonResponse,HttpResponse
from rest_framework import viewsets

def person_view(request):
    names={'name':'venkat','father':'lakshminarasaiah','mother':'polamma'}
    # api={'names':names}
    jsonn=json.dumps(names)
    return HttpResponse(jsonn,content_type='application/json')

class restapi(viewsets.ModelViewSet):
    queryset = person.objects.all()
    serializer_class = restapiselizer


