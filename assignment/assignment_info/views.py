from django.shortcuts import render
from .forms import SubmissionForm
from django.contrib.auth import get_user_model
from .models import Course,Submissions
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
# #
# class SubmissionFormView(CreateView):
#     model=Submission
#     fields=('answer','course')
#     template_name='submit.html'

@login_required
def SubmissionFormView(request,pk=None):
    submitted=False
    course=get_object_or_404(Course,pk=pk)
    if request.method=="POST":
        sub_form = SubmissionForm(request.POST or None,request.FILES or None)
        if sub_form.is_valid():
            form=sub_form.save(commit=False)
            form.user=request.user
            form.course=course
            form.save()
            submitted=True
    else:
        sub_form=SubmissionForm()
    return render(request,template_name='submit.html',context={
        'form':sub_form,
        'submitted':submitted
    })


class AssigmentList(ListView,LoginRequiredMixin):
    model=Course
    template_name='course_list.html'
