from django.http import HttpResponse
class infomiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request, *args, **kwargs):
        print('print pre pfrocessing ing request')
        res=self.get_response(request)
        print('afer response')
        return res
    def process_exception(self,request,exception):
        print('hai i am problem')
        # sa='<h1> meassage {} </h1>'.format(exception.__class__.__name)
        sa1='<h2> expection taype {}</h2>'.format(exception)
        return  HttpResponse(sa1)
