from django.urls import path
from .import views


app_name = "interviewer"

urlpatterns = [
    
    # /interviewer/Signup
    path('signup', views.InterviewerCreate, name='signup'),

    path('home', views.HomePage, name='home'),

    path('profile', views.profile, name='profile'),

    path('interviewsScheduled', views.interviewsScheduled, name='interviews-scheduled'),

    path('addinterviews', views.addinterviews, name='add-interviews'),

    path('interviewSceduled/<roomId>', views.gotoeditor, name='gotoeditor'),

]
