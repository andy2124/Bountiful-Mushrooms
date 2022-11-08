from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
app_name = "mushroom_app" 
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/item/', views.new_mushroom, name='new_mushroom'),
    path('accounts/delete/<int:mushroom_id>', views.delete, name='delete'),
    path('accounts/data/',views.mushroom_question, name='data' )
    
]
