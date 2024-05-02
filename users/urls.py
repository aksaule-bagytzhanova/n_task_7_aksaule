from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(next_page='/concerts'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/concerts'), name='logout'),
    path('register/', views.register, name='register'),
]
