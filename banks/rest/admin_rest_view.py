
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import AdminTokenObtainPairSerializer

class AdminLoginView(TokenObtainPairView):
    
    serializer_class = AdminTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        print("Admin login attempt")
        return super().post(request, *args, **kwargs)