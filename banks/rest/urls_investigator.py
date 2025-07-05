from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .investigator_rest_view import InvestigatorLoginView
from .common_rest_view import LogoutView

urlpatterns = [
    path('login/', InvestigatorLoginView.as_view(), name='investigator_login'),
    
    path('refresh/', TokenRefreshView.as_view(), name='investigator_token_refresh'),
  
    path('logout/', LogoutView.as_view(), name='investigator_logout'),
]
