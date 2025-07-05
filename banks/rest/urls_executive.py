from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .executive_rest_view import ExecutiveLoginView
from .common_rest_view import LogoutView

urlpatterns = [
    path('login/', ExecutiveLoginView.as_view(), name='executive_login'),
    
    path('refresh/', TokenRefreshView.as_view(), name='executive_token_refresh'),
   
    path('logout/', LogoutView.as_view(), name='executive_logout'),
]

