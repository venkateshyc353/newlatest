from django.urls import path
from . import views
urlpatterns=[
    path('info/',views.school_info,name='info')
]