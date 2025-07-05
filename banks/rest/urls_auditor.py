from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .auditor_rest_view import AuditorLoginView
from .common_rest_view import LogoutView

urlpatterns = [
    path('login/', AuditorLoginView.as_view(), name='auditor_login'),
    
    path('refresh/', TokenRefreshView.as_view(), name='auditor_token_refresh'),
   
    path('logout/', LogoutView.as_view(), name='auditor_logout'),
]
