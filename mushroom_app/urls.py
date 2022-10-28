from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
app_name = "mushroom_app" 
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/register/', views.register, name='register'),
    
]


    # path('accounts/logout/', views.user_logout, name='logout'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    # path('accounts/', include("django.contrib.auth.urls")),

    # path('profile/', views.profile, name='profile'),
    