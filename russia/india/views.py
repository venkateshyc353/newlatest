from django.shortcuts import render
from . models import schoolnames
from django.http import HttpResponse
from . ll import rest
from rest_framework.views import APIView
from rest_framework.response import  Response
import json
from .form import studentfrom
# from rest_framework import serializers
from django.views.generic import View
from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework import viewsets
def schoolchild(request):
    rr=schoolnames.objects.exclude(name='sirisha')
    kk={'rr':rr}
    if request.method=='POST':
        pp=studentfrom(request.POST)
        if pp.is_valid():
            print('after validation')
            print('name',pp.cleaned_data['name'])
            print('marksss',pp.cleaned_data['number'])

    pp=studentfrom()
    return render(request,'testapp/data.html',{'form':pp})
# Create your views here.
class api(viewsets.ModelViewSet):
    queryset =schoolnames.objects.all()
    serializer_class = rest
class resttapi(View):
    def get(request):
        data=schoolnames.objects.all()
        # dataa={'name':data.name,'father':data.father}
        kk=serialize('json',data)
        return HttpResponse(kk,content_type='application/json')
# def new(request):
    # aa=schoolnames.objects.all()
#     d=serialize('json',aa)
#     # print(d)
#     return render(request,'testapp/data.html',d)
#
# class testapiview(APIView):
#     def get(self,request,format=None):
#         colors=['red','green','blue']
#         return Response({'mes':'welcome','colors':colors})
