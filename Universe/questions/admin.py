from django.contrib import admin

from .models import Questions



class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model=Questions
admin.site.register(Questions,QuestionAdmin)
