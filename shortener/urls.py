from django.urls import path
from .views import redirect_view, create_short_link_api, get_link_stats_api

urlpatterns = [
    path('api/create/', create_short_link_api, name='api_create'),
    path('api/stats/<str:short_code>/', get_link_stats_api, name='api_stats'),
    path('<str:short_code>/', redirect_view, name='redirect'),
]