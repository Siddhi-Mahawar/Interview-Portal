from django.urls import path
from . import views

app_name = "editor"

urlpatterns = [

    # /editor
    path('/', views.Edit, name='editor'),

    path('/run', views.Run, name = 'run'),

]
