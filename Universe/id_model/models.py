from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class DateModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    key=models.PositiveIntegerField()
    time=models.DateTimeField()


    def __str__(self):
        return str(self.key)