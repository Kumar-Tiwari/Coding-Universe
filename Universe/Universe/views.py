from django.shortcuts import render
from django.contrib.auth import get_user_model

User=get_user_model()

def Base(request):
    try:
        session_id=request.session['user_id']
        user=User.objects.get(id=session_id)
        context={
            'name':user.username,
            'email':user.email
        }
        return render(request,'base.html',context)
    except :
        return render(request,'base.html',{})