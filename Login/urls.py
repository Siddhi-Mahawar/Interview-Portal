from django.urls import path
from .import views


app_name = "Login"

urlpatterns = [
    # /Login/
    path('/', views.IndexView.as_view(), name='index'),
    
    # /Login/person_id
    path('/<int:pk>', views.DetailView.as_view(), name='detail'),
    
    # /Login/Signup
    path('/signup/', views.AdminCreate, name='company-Admin-add'),
]
