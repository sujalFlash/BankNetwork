
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import AuditorTokenObtainPairSerializer

class AuditorLoginView(TokenObtainPairView):
 
    serializer_class = AuditorTokenObtainPairSerializer
