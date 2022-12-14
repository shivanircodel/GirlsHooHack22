"""testProjectSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from pages.views import homepage_view
from pages.views import LegalResources_view
from pages.views import MedicalResources_view
from pages.views import GetResourcesNearYou_view
from pages.views import Financial_Resources

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', homepage_view),
    path('legal_resources/', LegalResources_view),
    path('medical_resources/', MedicalResources_view),
    path('resources_near_you/', GetResourcesNearYou_view),
    path('financial_resources/', Financial_Resources)
]
