"""django_app URL Configuration

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
from django.urls import path, include

from rest_framework import routers
from sub_app.api.views import DgrPeriodsViewSet
from sub_app.api.views import TimeRulesViewSet
from sub_app.api.views import TwBlocksViewSet
from sub_app.api.views import TwForYearsViewSet


# api route
router = routers.DefaultRouter()
router.register(r'dgr_periods', DgrPeriodsViewSet,  basename='DgrPeriods')
router.register(r'time_rules', TimeRulesViewSet, basename='TimeRules')
router.register(r'tw_blocks', TwBlocksViewSet, basename='TwBlocks')
router.register(r'tw_for_years', TwForYearsViewSet, basename='TwForYears')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
