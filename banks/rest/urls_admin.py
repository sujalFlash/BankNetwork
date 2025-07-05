from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .admin_rest_view import AdminLoginView
from .common_rest_view import LogoutView

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='admin_login'),
    
    path('refresh/', TokenRefreshView.as_view(), name='admin_token_refresh'),
   
    path('logout/', LogoutView.as_view(), name='admin_logout'),
]
