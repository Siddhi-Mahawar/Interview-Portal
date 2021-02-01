from django.urls import path
from . import views

app_name = "editor"

urlpatterns = [

    # /editor
    path('/<roomId>', views.Edit, name='editor'),

    path('/run', views.Run, name = 'run'),

    path('/<roomId>/freeze', views.Freeze, name='freeze'),

    path('/<roomId>/check', views.Check, name='check'),

]
