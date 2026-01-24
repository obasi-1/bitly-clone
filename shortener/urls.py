from django.urls import path
from .views import redirect_view, home_view, create_short_link_api

urlpatterns = [
    # captures "wfx5GZ" as the variable 'short_code'
    path('', home_view, name='home'),
    path('api/create/', create_short_link_api, name='api_create'),
    path('<str:short_code>/', redirect_view, name='redirect'),
]