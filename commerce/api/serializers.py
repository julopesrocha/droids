from rest_framework import serializers
from commerce.models import models 

class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Demand
        fields = '__all__'