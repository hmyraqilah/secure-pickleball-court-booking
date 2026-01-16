from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

import logging
logger = logging.getLogger("security")

from ratelimit.decorators import ratelimit
from datetime import timedelta
from django.utils import timezone
import random

from .models import LoginOTP

User = get_user_model()


# 1. REGISTER VIEW
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


# 2. LOGIN VIEW WITH OTP
@ratelimit(key='ip', rate='5/m', block=True)
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # Generate OTP
            otp_code = str(random.randint(100000, 999999))

            # Save OTP
            LoginOTP.objects.create(user=user, otp=otp_code, created_at=timezone.now())

            # Send OTP to email (console backend)
            send_mail(
                subject="Your Login OTP",
                message=f"Your OTP code is: {otp_code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            # Store user ID temporarily
            request.session['otp_user_id'] = user.id
        else:
            #LOG FAILED LOGIN
            username = request.POST.get("username")
            logger.warning(
                f"Failed login attempt for username: {username} from IP {request.META.get('REMOTE_ADDR')}"
            )
            return redirect('otp_verify')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


# 3. OTP VERIFICATION VIEW
def otp_verify_view(request):
    user_id = request.session.get("otp_user_id")
    if not user_id:
        return redirect('login')

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login')

    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        
        # Get latest OTP in the last 5 minutes
        valid_time = timezone.now() - timedelta(minutes=5)
        otp_obj = LoginOTP.objects.filter(user=user, created_at__gte=valid_time).order_by('-created_at').first()

        if otp_obj and otp_obj.otp == entered_otp:
            login(request, user)
            otp_obj.delete()  # OTP used once
            del request.session['otp_user_id']
            return redirect('dashboard')
        #LOG OTP FAIL
        else:
         logger.warning(
             f"Suspicious activity: invalid OTP attempt for user {user.username} from IP {request.META.get('REMOTE_ADDR')}"
    )
    error = "Invalid or expired OTP."
    return render(request, 'accounts/otp_verify.html', {'error': error})


    return render(request, 'accounts/otp_verify.html')


# 4. DASHBOARD (LOGIN REQUIRED)
@login_required
def dashboard_view(request):
    if not request.user.is_authenticated:#LOG SUSPICIOUS ACTIVITY
        logger.warning(
            f"Suspicious activity: unauthorized dashboard access from IP {request.META.get('REMOTE_ADDR')}"
        )
    return render(request, 'accounts/dashboard.html')


# ===== TEST ERROR HANDLING =====
from django.core.exceptions import PermissionDenied

def test403(request):
    raise PermissionDenied

def test500(request):
    1/0   # sengaja buat error

from django.core.exceptions import BadRequest

def test400(request):
    raise BadRequest

