# banks/urls.py
from django.urls import path, include

urlpatterns = [
    # 1️⃣ Public (no‑auth) views
    path("",      include("banks.urls_public")),

    # 2️⃣ All REST endpoints (JWT‑protected), under /api/
    path("api/",  include("banks.urls_rest_view")),
]
