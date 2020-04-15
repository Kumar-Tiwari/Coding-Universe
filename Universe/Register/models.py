from django.db import models
from django.db.models.signals import post_save 
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils import timezone
import hashlib
import random

User=get_user_model()

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20 , blank=False , null=False)
    middle_name=models.CharField(max_length=20 , blank =True , null=True)
    last_name=models.CharField(max_length=20,blank=False,null=False)
    Student_ID=models.CharField(max_length=15,blank=False,null=False)
    Gender=models.CharField(choices=GENDER_CHOICES,max_length=20,blank=True,null=True)
    phone=models.PositiveIntegerField()
    Description=models.TextField()
    Profile_picture=models.ImageField(upload_to='Statics/Images',blank=True,null=True)

    def __str__(self):
        return str(self.Student_ID)


class EmailConfirm(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    key=models.CharField(max_length=10)
    date=models.DateTimeField()

    def __str__(self):
        return str(self.user)


def profile_save(sender,created,instance,**kwargs):
    if created:

        print(instance.username)
        short_hash=hashlib.sha1((str(random.random())+instance.username).encode('utf-8')).hexdigest()[:6]
        print(short_hash)
        email=instance.email
        subject="Please Verify Your Email"
        context={
            'key':short_hash,
            'username':instance.username,
        }
        message=render_to_string('Register/activation.html',context)

        send_mail(subject,message,'asdfghjkl.kt97@gmail.com',[email,],fail_silently=False)

        p=EmailConfirm.objects.create(user=instance,key=short_hash,date=timezone.now())
        p.save()

post_save.connect(profile_save,sender=User)