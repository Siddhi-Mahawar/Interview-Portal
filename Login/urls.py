from django.urls import path
from django.contrib.auth import views as auth_views
from .import views


app_name = "Login"

urlpatterns = [

    # /
    path('', views.LoginView, name='login'),
    
    # /home
    path('home', views.HomePage, name='home'),

    # /signup
    path('signup/', views.AdminCreate, name='company-Admin-add'),

    # /verify
    path('verify/', views.AdminEmailVerification, name='admin-email-verification'),

    # /verify/token_value
    path('verify/<token_value>', views.EmailVerify, name='admin-email-verify'),

    # /resetpassword
    path('resetpassword/', views.ResetPasswordRequest, name='password-reset-request'),

    # /resetpassword/token_value
    path('resetpassword/<token_value>', views.ResetPassword, name='password-reset'),

    # /interviewers
    path('interviewers', views.Interviewers, name='interviewers'),
    
    # /interviewees
    path('interviewees', views.Interviewees, name='interviewees'),

    # /logout
    path('logout', views.Logout, name='logout'),
    
]
