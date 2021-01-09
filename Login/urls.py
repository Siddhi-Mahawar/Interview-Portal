from django.urls import path
from .import views


app_name = "Login"

urlpatterns = [
    # /Login/
    path('/', views.LoginView, name='index'),
    
    # /Login/person_id
    path('/home', views.HomePage, name='home'),
    
    # /Login/Signup
    path('/signup/', views.AdminCreate, name='company-Admin-add'),

    # # /Login/Verify
    # path('/verify/', views.AdminEmailVerification, name='admin-email-verification'),
]
