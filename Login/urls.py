from django.urls import path
from .import views


app_name = "Login"

urlpatterns = [
    # /Login/
    path('/', views.index, name='index'),
    # /Login/person_id
    path('/<int:pk>', views.detail, name='detail'),
    # /Login/Signup
    path('/signup/', views.AdminCreate.as_view(), name='CompAdmin-add'),
]
