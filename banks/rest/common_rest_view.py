
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .serializers import TokenBlacklistSerializer

class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = TokenBlacklistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            token = RefreshToken(serializer.validated_data["refresh"])
            token.blacklist()
        except TokenError:
            return Response(
                {"detail": "Invalid or expired refresh token."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)