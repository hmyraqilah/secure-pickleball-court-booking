from django.urls import path
from . import views
from .views import register_view, login_view, dashboard_view, otp_verify_view

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('otp/', otp_verify_view, name='otp_verify'),
    path("test403/", views.test403),
    path("test500/", views.test500),
    path("test400/", views.test400),

]   