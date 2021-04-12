from django.urls import path
from .views import HomeView, UserLoginView, UserLogoutView, UserView
from . import views

app_name = 'accounts'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('regist/', views.regist, name='regist'),
    #path('user_login/', views.user_login, name='user_login'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
    path('user/', UserView.as_view(), name='user'),
]