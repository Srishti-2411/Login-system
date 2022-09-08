from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
    path('create_blog/',views.create_blog, name='create_blog'),
    path('show_blog/',views.show_blogs, name='show_blog'), 
    path('update_blog/<int:ok>',views.update, name='update_blog')    
]