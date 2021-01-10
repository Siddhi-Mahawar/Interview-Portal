from django.urls import path
from .import views


app_name = "interviewee"

urlpatterns = [
    
    # /interviewer/Signup
    path('/signup/', views.IntervieweeCreate, name='signup'),

    path('/home', views.HomePage, name='home'),

]
