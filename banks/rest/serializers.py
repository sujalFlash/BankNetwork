# banks/rest/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class RoleTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Base serializer that ensures the authenticated user has the expected role
    and injects role and professional_id into the token claims.
    """
    expected_role = None  # override in subclasses

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        prof = user.banking_profile
        token['role'] = prof.role
        token['professional_id'] = prof.professional_id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        prof = self.user.banking_profile
        if prof.role != self.expected_role:
            raise serializers.ValidationError(
                {'detail': f"User is not a {self.expected_role}."}
            )
        return data

class AnalystTokenObtainPairSerializer(RoleTokenObtainPairSerializer):
    """
    Serializer for Analyst login: only users with BankingProfessional.role == 'ANALYST'
    """
    expected_role = "ANALYST"
class InvestigatorTokenObtainPairSerializer(RoleTokenObtainPairSerializer):
    """
    Serializer for Investigator login: only users with BankingProfessional.role == 'INVESTIGATOR'
    """
    expected_role = "INVESTIGATOR"

class ExecutiveTokenObtainPairSerializer(RoleTokenObtainPairSerializer):
    """
    Serializer for Executive login: only users with BankingProfessional.role == 'EXECUTIVE'
    """
    expected_role = "EXECUTIVE"

class AdminTokenObtainPairSerializer(RoleTokenObtainPairSerializer):
    """
    Serializer for Admin login: only users with BankingProfessional.role == 'ADMIN'
    """
    expected_role = "ADMIN"

class AuditorTokenObtainPairSerializer(RoleTokenObtainPairSerializer):
    """
    Serializer for Auditor login: only users with BankingProfessional.role == 'AUDITOR'
    """
    expected_role = "AUDITOR"
class ComplianceTokenObtainPairSerializer(RoleTokenObtainPairSerializer):
    """
    Serializer for Compliance Officer login: only users with BankingProfessional.role == 'COMPLIANCE'
    """
    expected_role = "COMPLIANCE"
class TokenBlacklistSerializer(serializers.Serializer):
    """
    Serializer for blacklisting refresh tokens.
    """
    refresh = serializers.CharField(required=True)

    def validate(self, attrs):
        refresh_token = attrs.get('refresh')
        if not refresh_token:
            raise serializers.ValidationError(
                {'detail': 'Refresh token is required.'}
            )
        return attrs