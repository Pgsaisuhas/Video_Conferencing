from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup, name='register'),
    path('signin/',views.signin, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('meeting/',views.conferencing, name='meeting'),
    path('signout/',views.signout, name='logout'),
    path('join/',views.join, name='join'),

]