from django.shortcuts import  render
from . forms import schoolform
def school_info(request):
    if request.method=='POST':
        infoo=schoolform(request.POST)
        print(10/0)
        if infoo.is_valid():
            print(infoo.cleaned_data['name'])
            print(infoo.cleaned_data['number'])
            print(infoo.cleaned_data['salary'])
            print(infoo.cleaned_data['viage'])
            print('hai venkat')

    go=schoolform()
    return  render(request,'testapp/register.html',{'go':go})
