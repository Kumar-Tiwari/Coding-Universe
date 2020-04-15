from django.contrib import admin
from .models import Profile,EmailConfirm

class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model=Profile


class EmailAdmin(admin.ModelAdmin):
    class Meta:
        model=EmailConfirm

        

admin.site.register(Profile,ProfileAdmin)
admin.site.register(EmailConfirm,EmailAdmin)
