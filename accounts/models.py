from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ============================
# Email Verification Model
# ============================
class EmailVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Verified: {self.verified}"


# ============================
# Login OTP Model
# ============================
class LoginOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.user.username}"
