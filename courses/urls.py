from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'), 
    path('', views.index, name='home'),
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.course_list, name='course_list'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    

]
