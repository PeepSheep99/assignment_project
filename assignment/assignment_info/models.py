from django.db import models
from django.conf import settings
from django.urls import reverse




class Course(models.Model):
    name=models.CharField(max_length=30,blank=False)
    code=models.CharField(max_length=10,unique=True)
    question=models.TextField(blank=False)
    deadline_date=models.DateField(null=True)
    deadline_time =models.TimeField(null=True)

    def __str__(self):
        return "{}-{}".format(self.code,self.name)





# class CourseForm(ModelForm):
#     class Meta():
#         model=Course
#         fields=('name','code','question','deadline_date')


class Submissions(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default=1)
    answer=models.FileField(upload_to='assignments/{}'.format(course.name))
    submitted_at=models.DateTimeField(auto_now=True,blank=False)


    def get_absolute_url(self):
        return reverse('assignments:list')

    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:
    #     # Only set added_by during the first save.
    #         obj.user = request.user
    #     super().save_model(request, obj, form, change)


    # def __init__(self, *args, **kwargs):
    #     user_id = kwargs.pop('user_id')
    #     super(SubmissionForm, self).__init__(*args, **kwargs)
    #     user = User.objects.get(id=user_id)
    #     self.fields['user'].queryset = user

    def __str__(self):
        return "{}-{}".format(self.user.username,self.user.first_name+' '+self.user.last_name)
