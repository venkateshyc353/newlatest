from django.contrib import admin
from .models import schoolmodel

class model(admin.ModelAdmin):
    list_display = ['name','mobile','addres']
admin.site.register(schoolmodel,model)