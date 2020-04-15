from django import forms
from .models import Profile
from django.contrib.auth import get_user_model
from .models import GENDER_CHOICES
from datetime import date

User=get_user_model()


class AuthenticationForm(forms.ModelForm):
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "name":"UserName", "id":"UserName", "required placeholder":"eg.name123*"
    }))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={
        "name":"PassWord","id":"PassWord","required placeholder":"********"
    }))
    confirm_password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={
        "name":"PassWord","id":"PassWord","required placeholder":"********"
    }))
    email=forms.CharField(max_length=100,widget=forms.EmailInput(attrs={
        "name":"Email","id":"Email","required placeholder":"eg.name123@abc.com*"
    }))
    class Meta:
        model=User
        fields=['username','email','password']

    def clean_confirm_password(self):
        confirm_password=self.cleaned_data.get("confirm_password")
        password=self.cleaned_data.get("password")
        print(password)
        print(confirm_password)
        if password != confirm_password:
            raise forms.ValidationError("Password didn't match")
        return password

    def clean_username(self):
        username=self.cleaned_data.get("username")
        username1=User.objects.filter(username=username)

        if username1.exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email=self.cleaned_data.get("email")
        email1=User.objects.filter(email=email)

        if email1.exists():
            raise forms.ValidationError("Email is already taken")
        return email

    def save(self,commit=True):
        user=super(AuthenticationForm,self).save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        user.is_active=False
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "name":"FirstName", "id":"FirstName", "required placeholder":"First Name*"
    }))
    middle_name=forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={
        "name":"MiddleName", "id":"MiddleName", "placeholder":"Middle Name*"
    }))
    last_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "name":"LastName", "id":"LastName", "required placeholder":"Last Name*"
    }
    ))
    Student_ID=forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "name":"StudentID", "id":"StudentID", "required placeholder":"THA075BCT023*"
    }))
    Gender=forms.CharField(max_length=20,widget=forms.Select(choices=GENDER_CHOICES))

    phone=forms.CharField(max_length=20,widget=forms.TextInput())
    Description=forms.CharField(max_length=20,widget=forms.Textarea(attrs={
        "name":"Description", "id":"Description", "cols":"30", "rows":"5" ,"placeholder":"Write about yourself"
    }
    ))
    class Meta:
        model=Profile
        exclude=['user']

    def clean_Student_ID(self):
        student_id=self.cleaned_data.get("Student_ID")
        student_id1=Profile.objects.filter(Student_ID=student_id)
        if student_id1.exists():
            raise forms.ValidationError("Student with this ID is already registered")
        if not 'THA' in student_id:
            raise forms.ValidationError("Error in Student_ID")
        return student_id

class Activate(forms.Form):
    activation_key=forms.CharField(max_length=6,widget=forms.TextInput(attrs={
        "name":"Activation Key", "id":"Activation", "required placeholder":"eg.ax237*"
    }))

class LoginForm(forms.Form):
    username=forms.CharField(required=True,max_length=30,widget=forms.TextInput(attrs={
        "name":"Username" ,"id":"Username" ,"required placeholder":"Username"
    }))
    password=forms.CharField(required=True,max_length=30,widget=forms.PasswordInput(attrs={
        "name":"PassWord", "id":"PassWord","required placeholder":"Password"
    }))

    def clean_username(self):
        username=self.cleaned_data.get("username")
        print(username)
        try:
            User.objects.get(username=username)
        except User.DoesNotExist :
            raise forms.ValidationError("Username doesnot exist")
        return username
