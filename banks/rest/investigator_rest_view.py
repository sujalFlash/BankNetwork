# banks/rest/analyst_rest_view.py
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import InvestigatorTokenObtainPairSerializer


class InvestigatorLoginView(TokenObtainPairView):
    serializer_class = InvestigatorTokenObtainPairSerializer
    



