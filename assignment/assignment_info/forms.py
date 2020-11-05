from django import forms
from .models import Submissions


class SubmissionForm(forms.ModelForm):
    class Meta():
        fields=('answer',)
        model=Submissions

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['answer']='Upload your file'
