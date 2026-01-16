from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseBadRequest
from django.core.exceptions import PermissionDenied

def test400(request):
    return HttpResponseBadRequest("Bad request")

def test403(request):
    raise PermissionDenied

def test500(request):
    1/0

from django.shortcuts import render

def custom_400(request, exception=None):
    return render(request, "400.html", status=400)