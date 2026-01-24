from django.db import models
from .utils import generate_short_code  # Import your new function

class Link(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # If no code exists, generate one
        if not self.short_code:
            while True:
                new_code = generate_short_code()
                # Check if this code already exists in the DB
                if not Link.objects.filter(short_code=new_code).exists():
                    self.short_code = new_code
                    break
                    
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"