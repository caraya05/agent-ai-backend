from django.urls import include, path
from rest_framework import routers

from companies.viewset.company_viewset import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
]
