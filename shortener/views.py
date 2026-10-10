from django.shortcuts import get_object_or_404, redirect
from django.db.models import F
from .models import Link
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import LinkSerializer



def redirect_view(request, short_code):
    # 1. Get the link (or return 404 if not found)
    link = get_object_or_404(Link, short_code=short_code)
    
    # 2. Increment clicks safely using F expression (Race-condition proof)
    link.clicks = F('clicks') + 1
    link.save()
    
    # 3. Send them to the destination
    return redirect(link.original_url)

@swagger_auto_schema(method='post', request_body=LinkSerializer)  # <-- THIS LINE FIXES IT
@api_view(['POST'])

def create_short_link_api(request):
    """
    API Endpoint: Accepts JSON {'original_url': '...'} and returns short link.
    """
    serializer = LinkSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Add this below your existing create_short_link_api view
@api_view(['GET'])
def get_link_stats_api(request, short_code):
    """
    API Endpoint: Returns the click count and original URL for a given short code.
    """
    # Grab the link or return a 404 if it doesn't exist
    link = get_object_or_404(Link, short_code=short_code)
    
    return Response({
        'short_code': link.short_code,
        'original_url': link.original_url,
        'clicks': link.clicks
    }, status=status.HTTP_200_OK)