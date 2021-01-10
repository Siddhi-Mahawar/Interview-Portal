from django.urls import path
from .import views

app_name = "Users"

urlpatterns = [
    # /Login/
    path('/', views.LoginView, name='index'),
]
