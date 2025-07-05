from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .analyst_rest_view import AnalystLoginView
from .common_rest_view import LogoutView

urlpatterns = [
    path('login/', AnalystLoginView.as_view(), name='analyst_login'),
    
    path('refresh/', TokenRefreshView.as_view(), name='analyst_token_refresh'),
    # POST /api/analyst/logout/  -> blacklists the refresh token
    path('logout/', LogoutView.as_view(), name='analyst_logout'),
]
