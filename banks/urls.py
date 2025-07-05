from django.urls import path, include

urlpatterns = [
    # non‑auth pages:
    path('', include('banks.urls_public')),
    # all JWT‑protected REST endpoints:
    path('api/', include('banks.urls_rest')),
]
