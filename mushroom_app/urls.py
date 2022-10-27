from django.urls import path
from . import views
app_name = "mushroom_app" 
urlpatterns = [
    path('mushroom/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    # path('profile/', views.profile, name='profile'),
    
    #  path('', views.home, name='home'),
    # path('profile/<str:username>', views.profile, name='profile'),
    

]
