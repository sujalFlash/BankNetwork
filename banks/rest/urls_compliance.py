from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .compliance_rest_view import ComplianceLoginView
from .common_rest_view import LogoutView

urlpatterns = [
    path('login/', ComplianceLoginView.as_view(), name='compliance_login'),
    
    path('refresh/', TokenRefreshView.as_view(), name='compliance_token_refresh'),
   
    path('logout/', LogoutView.as_view(), name='compliance_logout'),
]
