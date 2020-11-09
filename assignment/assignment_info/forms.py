from django import forms
from .models import Submissions,Course





class CourseForm(forms.ModelForm):
    name=forms.CharField(max_length=100)
    code=forms.CharField(max_length=100)
    question=forms.CharField(widget=forms.Textarea)
    deadline_date=forms.DateField(widget=forms.SelectDateWidget)
    deadline_time=forms.TimeField()
    class Meta():
        model=Course
        fields=('name','code','question','deadline_date','deadline_time')

class SubmissionForm(forms.ModelForm):
    class Meta():
        fields=('answer',)
        model=Submissions

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['answer']='Upload your file'
