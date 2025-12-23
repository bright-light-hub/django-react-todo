from django import forms
from  . models import TODO

class TodoForms(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'is_complete']