from django.urls import path
from . import  views
from rest_framework import routers
# kk=routers.DefaultRouter()
# kk.register('testapp',views.restapi)
urlpatterns=[
    # path('info/',views.student_info,name='schoolapp'),
    # path('api',include(kk.urls)),
    path('form',views.school_from),
    # path('kl',views.school_info)
]
