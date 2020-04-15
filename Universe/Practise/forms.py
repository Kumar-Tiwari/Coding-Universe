from django import forms

LANGUAGE = (
   ('python3', 'Python'),
   ('c', 'C'),
   ('cpp', 'C++')
)
class SubmissionForm(forms.Form):
    solution=forms.CharField(max_length=10000,widget=forms.Textarea(attrs={
        "class":"form-control", "id":"exampleFormControlTextarea5", "rows":"3"
    }))
    language=forms.CharField(max_length=20,widget=forms.Select(choices=LANGUAGE))