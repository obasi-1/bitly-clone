from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from .models import Link
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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

@api_view(['POST'])
def create_short_link_api(request):
    """
    API Endpoint: Accepts JSON {'original_url': '...'} and returns short link.
    """
    # 1. Pass the data to the serializer (The Translator)
    serializer = LinkSerializer(data=request.data)
    
    # 2. Validate (Is it a real URL?)
    if serializer.is_valid():
        # 3. Save (The Model's save() method will still trigger and generate the code!)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 4. Error handling
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)