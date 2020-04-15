from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from Register.models import Profile
from django.contrib.auth.decorators import login_required

User=get_user_model()

def Home(request):
    try:
        session_id=request.session['user_id']
        u1=User.objects.get(id=session_id)
        p1=Profile.objects.get(user=session_id)
        context={
            'u1':u1,
            'p1':p1,
            'verify':'True',
        }
        return render(request,'Home/home.html',context)
    except :
        context={
            'verify':'False',
            'new':'new'
        }
        return render(request,'Home/home.html',context)


@login_required
def Search(request):
    session_id=request.session['user_id']
    u1=User.objects.get(id=session_id)
    p1=Profile.objects.get(user=session_id)
    search_key=request.GET.get('k')
    context={
        'key':search_key,
        'u1':u1,
        'p1':p1,
        'verify':'True',
    }
    return render(request,'Home/search.html',context)
    # search_key=request.GET.get('k')
    # print(search_key)
    # return redirect('/')
    
