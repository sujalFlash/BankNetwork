# banks/urls_rest_view.py
from django.urls import path, include
from .views import index
urlpatterns = [
 path("public/",index,name="index"),  # Public view
]
