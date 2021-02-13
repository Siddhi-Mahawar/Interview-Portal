from django.urls import path
from .import views


app_name = "interviewee"

urlpatterns = [
    
    # /interviewer/Signup
    path('signup', views.IntervieweeCreate, name='signup'),

    path('home', views.Profile, name='home'),

    path('details', views.IntervieweeDetails, name='details'),

    path('interviewsScheduled', views.interviewsScheduled, name='interviews-scheduled'),

]
