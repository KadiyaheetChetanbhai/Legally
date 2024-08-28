from django.urls import path
from .views import query_legal_info

urlpatterns = [
    path('query-legal-info/', query_legal_info, name='query_legal_info'),
]
