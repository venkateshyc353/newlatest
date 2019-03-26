from django.http import HttpResponse
class loginmiddle(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request, *args, **kwargs):
        print('before fre processing request')
        response=self.get_response(request)
        print('after fre frocessing request')
        return response
    def process_exption(self,request,exception):
        print('before fre proce')
        # l='exception type {}'.format(exception.__class__.__name__)
        k='ex[pvv'.format(exception)
        return HttpResponse(l+k)