from django.urls import path
from .import views


app_name = "interviewer"

urlpatterns = [
    
    # /interviewer/Signup
    path('/signup/', views.InterviewerCreate, name='signup'),

]
