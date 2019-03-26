from django.http import  HttpResponse
class loginmiddle(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request, *args, **kwargs):
        print('pree processing requiest')
        req=self.get_response(request)
        print('after processing request')
        return req
        # return HttpResponse('application under maintance')

    def proce_exception(self,request,exception):
        print('tell me which type of request')
        a=print('this is error : {}'.format(exception.__class__.__name__))
        return HttpResponse(a)