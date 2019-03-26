from django.contrib import admin
from django.urls import path,include
from . import views
# from django i
from rest_framework import routers
ro=routers.DefaultRouter()
ro.register('smaank',views.restapi)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.person_view),
    path('api/',include(ro.urls))
]