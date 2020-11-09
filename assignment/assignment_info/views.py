from django.shortcuts import render
from .forms import SubmissionForm,CourseForm
from django.contrib.auth import get_user_model
from .models import Course,Submissions
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
import datetime
from django.urls import reverse_lazy


@login_required
def SubmissionFormView(request,pk=None):
    submitted=False
    current_time=datetime.datetime.now()
    course=get_object_or_404(Course,pk=pk)
    if request.method=="POST":
        sub_form = SubmissionForm(request.POST or None,request.FILES or None)
        if sub_form.is_valid():
            form=sub_form.save(commit=False)
            form.user=request.user
            form.course=course
            form.submitted_at=datetime.datetime.now()
            # if 'answer' in request.FILES:
            if 'answer' in request.FILES:
                form.answer=request.FILES['answer']
            form.save()
            submitted=True
    else:
        sub_form=SubmissionForm()
    return render(request,template_name='submit.html',context={
        'form':sub_form,
        'submitted':submitted,
        'course':course,
        'current_time':current_time,
    })

#
def CourseView(request):
    created=False

    if request.method=='POST':
        course_form=CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save(commit=True)
            created=True
            # form.deadline_date=form.d_date
        else:
            print(course_form.errors)
    else:
        course_form=CourseForm()
    return render(request,'course_form.html',context={
        'form':course_form,
        'created':created
    })


class AssigmentList(ListView,LoginRequiredMixin):
    model=Course
    template_name='course_list.html'

# class CourseDetailView(DetailView):
#     model=Course
#     template_name='course_detail.html'
