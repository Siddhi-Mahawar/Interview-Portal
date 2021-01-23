from django.urls import path
from . import views

app_name = "editor"

urlpatterns = [

    # /interviewer/Signup
    path('/', views.Edit, name='editor'),

]
