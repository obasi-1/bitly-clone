from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['original_url', 'short_code', 'clicks', 'created_at']
        read_only_fields = ['short_code', 'clicks', 'created_at']