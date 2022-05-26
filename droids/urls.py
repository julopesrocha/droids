from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from commerce.api.viewsets import DemandViewSet


router = routers.DefaultRouter()

router.register(r'demand', DemandViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
