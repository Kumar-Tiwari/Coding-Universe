from django.shortcuts import render,redirect
from .forms import AuthenticationForm
from .forms import ProfileForm,Activate
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import EmailConfirm
from django.contrib.auth import get_user_model
from django.contrib.auth import logout

User=get_user_model()
# import random
# import hashlib

def SignupView(request):
    try:
        session_id=request.session['user_id']
        return redirect('/')
    except:

        if request.method=="POST":
            user_form=AuthenticationForm(request.POST)
            profile_form=ProfileForm(request.POST or None , request.FILES or None)

            if user_form.is_valid() and profile_form.is_valid():
                user=user_form.save(commit=True)
                user.save()
                profile=profile_form.save(commit=False)
                profile.Profile_picture=profile_form.cleaned_data.get("Profile_picture")
                profile.user=user
                profile.save()
                # request.session['activation_id']=user.id
            # short_hash=hashlib.sha1((str(random.random())+user.username+profile.first_name).encode('utf-8')).hexdigest()[:6]
                return redirect('activate/')

            else:
             return render(request,'Register/signup.html',{'user_form':user_form,'profile_form':profile_form})
        else:
            user_form=AuthenticationForm()
            profile_form=ProfileForm()
            return render(request,'Register/signup.html',{'user_form':user_form,'profile_form':profile_form})

def ActivateView(request):

        # if request.method=="POST":
        #     form=Activate(request.POST)
        #     if form.is_valid():
        #         activation_key=form.cleaned_data.get("activation_key")
        #         print(activation_key)
        #         user=User.objects.get(id=activation_id)
        #         profile=EmailConfirm.objects.get(user=user.id)
        #         if profile.key == activation_key :
        #             user.is_active=True
        #             profile.key='activated'
        #             del request.session['activation_id']
        #             return redirect('login')
        #         else:
        #             context={
        #                 'form':Activate,
        #                 'error':'Activation_key error'
        #             }
        #             return render(request,'Reister/activate.html',context)
    return render(request,'Register/activate.html',{'form':Activate})


    

    # if request.method=="POST":
    #     form=Activate(request.POST)
    #     if form.is_valid():




def LoginView(request):
    try:
        session_id=request.session['user_id']
        return redirect('/')
    except:

        if request.method=="POST":
            form=LoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data.get("username")
                password=form.cleaned_data.get("password")
                user=authenticate(username=username , password=password)
                if user is not None:
                    request.session['user_id']=user.id
                    login(request,user)
                    return redirect('/')
                else:
                    context={
                        'form':form,
                        'error':' Either Password didnt match or Email is not confirmed'
                    }
                    return render(request,'Register/login.html',context)
            return render(request,'Register/login.html',{'form':form})
                
        return render(request,'Register/login.html',{'form':LoginForm})
        
    