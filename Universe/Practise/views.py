import json
import requests
from django.shortcuts import render,reverse,redirect
from Register.models import Profile
from id_model.models import DateModel
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from questions.models import Questions
from id_model.forms import AcceptForm
from django.utils import timezone
from datetime import timedelta
from .forms import SubmissionForm
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


User=get_user_model()

@login_required
def PractiseView(request):

    if request.method=="GET":
        session_id=request.session['user_id']
        u1=User.objects.get(id=session_id)
        p1=Profile.objects.get(user=session_id)

        try:
            b1=DateModel.objects.get(user=session_id)
            run_time=b1.time
            key_id=b1.key
            try:
                q1=Questions.objects.get(id=key_id)
                b1.key=key_id
                context={
                    'u1':u1,
                    'p1':p1,
                    'verify':'True',
                    'question':q1,
                    'form1':SubmissionForm,
                }   
                return render(request,'Practise/practise.html',context)
            except:
                context={
                    'u1':u1,
                    'p1':p1,
                    'verify':'True',
                    'question':'False'
                }   
                return render(request,'Practise/practise.html',context)



        except:

            context={
                'u1':u1,
                'p1':p1,
                'verify':'True',
                'form':AcceptForm
            }   
            return render(request,'Practise/front.html',context)

    if request.method=="POST":
        form=AcceptForm(request.POST)
        if form.is_valid():
            response=form.cleaned_data.get("checkbox")
            if response:
                session_id=request.session['user_id']
                u1=User.objects.get(id=session_id)
                p1=Profile.objects.get(user=session_id)
                b1=DateModel.objects.create(user=u1,key=1,time=timezone.now())
                q1=Questions.objects.get(id=1)
                context={
                'u1':u1,
                'p1':p1,
                'verify':'True',
                'question':q1,
                'key':'1',
                'form1':SubmissionForm,
                }   
                return render(request,'Practise/practise.html',context)
@login_required
@require_POST
def Result(request):
    session_id=request.session['user_id']
    u1=User.objects.get(id=session_id)
    p1=Profile.objects.get(user=session_id)
    d1=DateModel.objects.get(user=session_id)
    q1=Questions.objects.get(id=d1.key)
    try:
        form=SubmissionForm(request.POST)
        if form.is_valid():
            solution=form.cleaned_data.get("solution")
            language=form.cleaned_data.get("language")
            print(language)
            url="https://api.jdoodle.com/v1/execute"
            input_statement={
                'q1':q1
            }
            message_input=render_to_string("Practise/data.html",input_statement)
            data={
                "script":solution,
                "language":language,
                "versionIndex":"3",
                "stdin": message_input ,
                "clientId":"75d651edf787505a26809b980fbcc17d",
                "clientSecret": "d0be13039ba3b10b84bca88facdad3897b99d5a571a5e48711a4648b08d17e8c",

            }
            r=requests.post(url,json=data)
            b=r.json()
            output=b['output']
            status_code=b['statusCode']

            if status_code==200 :
                string=''
                for i in output :
                    if i != '\n':
                        string=string+i
                    else:
                        string=string+' '
                string=string.upper()
                string=string.split()
                if string[0]==q1.question_1_sample_output_1 and string[1]==q1.question_1_sample_output_2 and string[2]==q1.question_1_sample_output_3 :
                    print("reached_if")
                    d1.key=d1.key+1
                    d1.save()

                    return redirect('/practise/')
                else:
            
                    return redirect('/practise/')

    except:
        pass