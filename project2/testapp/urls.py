from django.urls import path,include
from. import views
from rest_framework import routers
dd=routers.DefaultRouter()
dd.register('testapp',views.restapi)
urlpatterns=[
    path('in/',views.schoolview),
    path('linfo/',views.formmm),
    path('rinfo/',views.datatable),
    path('api',include(dd.urls))
]