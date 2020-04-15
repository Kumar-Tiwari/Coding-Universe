from django import forms


class AcceptForm(forms.Form):
    checkbox=forms.BooleanField(widget=forms.CheckboxInput(attrs={
        "class":"custom-control-input", "id":"customCheck", "name":"example1"
    }))