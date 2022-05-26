from rest_framework import viewsets
from commerce.api import serializers
from commerce.models import models

class DemandViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DemandSerializer
    queryset = models.Demand.objects.all()