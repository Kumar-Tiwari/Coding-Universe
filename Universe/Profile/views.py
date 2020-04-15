from django.shortcuts import render,reverse
from Register.models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User=get_user_model()

@login_required
def ProfileView(request,name):
    
    session_id=request.session['user_id']
    u1=User.objects.get(id=session_id)
    p1=Profile.objects.get(user=session_id)
    u2=User.objects.get(username=name)
    p2=Profile.objects.get(user=u2.id)

    context={
        'u1':u1,
        'p1':p1,
        'p2':p2,
        'verify':'True',
        'u2':u2
    }
    return render(request,'Profile/profile.html',context)