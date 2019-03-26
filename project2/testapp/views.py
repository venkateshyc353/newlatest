from .serlizer import api
from rest_framework import viewsets
from django.shortcuts import render
from . models import schoolmodel
from .forms import schoolform
def schoolview(request):
    return render(request,'testapp/info.html')
def formmm(request):
    form=schoolform()
    if request.method=='POST':
        form=schoolform(request.POST)
        if form.is_valid():
            form.save()
            return schoolview(request)
    return render(request,'testapp/forms.html',{'form':form})
def datatable(request):
    dataa=schoolmodel.objects.all().order_by()
    return render(request,'testapp/table.html',{'dataa':dataa})
class restapi(viewsets.ModelViewSet):
    queryset = schoolmodel.objects.all()
    serializer_class = api
