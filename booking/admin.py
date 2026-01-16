from django.contrib import admin

# Register your models here.

import logging
from django.contrib import admin
from .models import CourtBooking

logger = logging.getLogger("security")

@admin.register(CourtBooking)
class CourtBookingAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        action = "UPDATED" if change else "CREATED"
        logger.info(f"Admin action: {action} booking by {request.user}")
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        logger.warning(f"Admin action: DELETED booking by {request.user}")
        super().delete_model(request, obj)

