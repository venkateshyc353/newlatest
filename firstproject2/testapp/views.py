from django.shortcuts import render
from  . models import schoolapp
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
import json
from .selizer import webapi
from rest_framework import viewsets
from  . forms import schoolform

# def student_info(request):
#     data=schoolapp.objects.all()
#     dat={'data':data}
#     return render(request,'testapp/info.html',dat)
#
#
# class restapi(viewsets.ModelViewSet):
#     queryset = schoolapp.objects.all()
#     serializer_class =webapi
def school_from(request):
    if request.method=='POST':
        da=schoolform(request.POST)
        if da.is_valid():
            print(da.cleaned_data['name'])
            print(da.cleaned_data['number'])
            print(da.cleaned_data['feedback'])
            print(da.cleaned_data['salary'])
            # print('hai venkat')
    da=schoolform()
    return render(request,'testapp/info.html',{'da':da})
