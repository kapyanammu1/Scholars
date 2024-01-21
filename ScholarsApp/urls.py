from django.contrib.auth import views as auth_views
from django.urls import path
from django_select2 import views as select2_views
from . import views
# from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    # path('Signup>/', views.Signup, name='Signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    # path('logout/', views.logout_view, name='logouts'),
    path('MunList/', views.MunList, name='MunList'),
    path('AdEdMun/<int:pk>/', views.AdEdMun, name='AdEdMun'),
    path('DelMun/<int:pk>/', views.DelMun, name='DelMun'),
]