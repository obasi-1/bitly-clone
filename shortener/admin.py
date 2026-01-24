from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    # This makes the columns visible in the list view
    list_display = ('original_url', 'short_code', 'clicks', 'created_at')
    
    # This makes 'clicks' read-only so you can't accidentally fake analytics
    readonly_fields = ('clicks',)