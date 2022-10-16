from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def homepage_view(request, *args, **kwargs):
    return render(request, "Home.html", {})

def LegalResources_view(request, *args, **kwargs):
    return render(request, "LegalResources.html", {})

def MedicalResources_view(request, *args, **kwargs):
    return render(request, "MedicalResources.html", {})

def GetResourcesNearYou_view(request, *args, **kwargs):
    return render(request, "ResourcesNearYou.html", {})

def Financial_Resources(request, *args, **kwargs):
    return render(request, "FinancialResources.html", {})
