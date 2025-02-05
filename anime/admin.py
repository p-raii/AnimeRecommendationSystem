from django.contrib import admin
from .models import AnimeData

class YourModelAdmin(admin.ModelAdmin):
    # Ensure deletion is allowed by default or by not overriding this method

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(AnimeData, YourModelAdmin)