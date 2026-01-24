from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from .models import Link
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import LinkSerializer

def home_view(request):
    context = {}
    
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        if original_url:
            link = Link.objects.create(original_url=original_url)
            
            # Pass the new short link to the template
            # We build the full URL (e.g., http://localhost:8000/AbCdEf)
            full_short_url = request.build_absolute_uri('/') + link.short_code
            context['new_link'] = full_short_url
            context['original_url'] = original_url

    return render(request, 'shortener/home.html', context)

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