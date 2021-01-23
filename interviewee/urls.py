from django.urls import path
from .import views


app_name = "interviewee"

urlpatterns = [
    
    # /interviewer/Signup
    path('/signup/', views.IntervieweeCreate, name='signup'),

    path('/home', views.HomePage, name='home'),

    path('/details', views.IntervieweeDetails, name='details'),

    path('/profile', views.profile, name='profile'),

    path('/interviewsScheduled', views.interviewsScheduled, name='interviews-scheduled'),

    path('/interviewRequests', views.interviewRequests, name='interview-requests'),

]
