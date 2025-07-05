# banks/urls_rest_view.py
from django.urls import path, include

urlpatterns = [
    path("analyst/",      include("banks.rest.urls_analyst")),
    path("investigator/", include("banks.rest.urls_investigator")),
    path("compliance/",   include("banks.rest.urls_compliance")),
    path("admin/",        include("banks.rest.urls_admin")),
    path("auditor/",      include("banks.rest.urls_auditor")),
    path("executive/",    include("banks.rest.urls_executive")),
]
