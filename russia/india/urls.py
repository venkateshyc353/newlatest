from django.urls import path,include
from . import views
from rest_framework import routers
a=routers.DefaultRouter()
a.register('india',views.api)
urlpatterns=[
    path('name',views.schoolchild),
    path('api/',include(a.urls)),
    path('jj',views.resttapi),
    # path('new',views.new,name='new'),
    # path('ap',views.testapiview,name='ap')
]