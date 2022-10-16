from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def homepage_view(request, *args, **kwargs):
    return render(request, "Home.html", {})

def LegalResources_view(request, *args, **kwargs):
    return render(request, "LegalResources.html", {})

def MedicalResources_view(request, *args, **kwargs):
    return render(request, "MedicalResources.html", {})