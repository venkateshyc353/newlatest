from django.http import HttpResponse
class loginmiddelware(object):
    def __init__(self,get_response):
        self.a=get_response
    def __call__(self,reques, *args, **kwargs):
        print('pre frocdceing middelware')
        resp=self.a(reques)
        print('after views')
        return HttpResponse('site maintance')

    def procee_expetion(self,request,exption):
        # a=('this what of error {}'.format(exption.__class__.__name__))
        # b=('exption type {}'.format(exption))
        return HttpResponse('site is maintance')