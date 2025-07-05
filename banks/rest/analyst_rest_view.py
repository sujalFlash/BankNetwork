
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import AnalystTokenObtainPairSerializer

class AnalystLoginView(TokenObtainPairView):
 
    serializer_class = AnalystTokenObtainPairSerializer
