from django.urls import path
from . import views

urlpatterns = [
    path("test400/", views.test400, name="test400"),
    path("test403/", views.test403, name="test403"),
    path("test500/", views.test500, name="test500"),
]
