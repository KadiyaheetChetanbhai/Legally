from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.legal_query, name='legal_query')
]
