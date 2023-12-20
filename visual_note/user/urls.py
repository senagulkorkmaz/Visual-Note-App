from user import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='user-register'),
    path('login/', views.LoginAPIView.as_view(), name="user-login"),
    path('logout/', views.LogoutAPIView.as_view(), name="user-login"),
    path('update/', views.UpdateAPIView.as_view(), name="user-update"),
]