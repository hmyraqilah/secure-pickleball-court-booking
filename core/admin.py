from django.contrib import admin

# Register your models here.
#ADMIN ACTION LOG
import logging
from django.contrib.admin.models import LogEntry
from django.db.models.signals import post_save
from django.dispatch import receiver

logger = logging.getLogger("security")

@receiver(post_save, sender=LogEntry)
def log_admin_actions(sender, instance, created, **kwargs):
    if created and instance.user:
        action = instance.get_action_flag_display()
        logger.info(f"Admin action: {action} by {instance.user}")
