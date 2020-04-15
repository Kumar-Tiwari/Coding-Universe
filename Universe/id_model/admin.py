from django.contrib import admin
from .models import DateModel



class DateAdmin(admin.ModelAdmin):
    class Meta:
        model=DateModel

admin.site.register(DateModel,DateAdmin)