from django.urls import path
from . import views
app_name='assignments'
urlpatterns=[
    path('', views.AssigmentList.as_view(),name='list'),
    path('submit/<int:pk>/', views.SubmissionFormView,name='submit'),
    path('create_assignment/', views.CourseView, name='create'),
]
