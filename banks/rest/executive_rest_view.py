
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ExecutiveTokenObtainPairSerializer

class ExecutiveLoginView(TokenObtainPairView):
 
    serializer_class = ExecutiveTokenObtainPairSerializer
