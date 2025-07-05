# banks/rest/analyst_rest_view.py
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import ComplianceTokenObtainPairSerializer

class ComplianceLoginView(TokenObtainPairView):

    serializer_class = ComplianceTokenObtainPairSerializer

