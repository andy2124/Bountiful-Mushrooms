from django.urls import path
from . import views
appname = 'mushroom_list'
urlpatterns = [
    path('mushroom/', views.index, name='index'),
    #  path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),

]