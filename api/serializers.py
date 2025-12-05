from rest_framework import serializers
from .models import Mpikambana,Sampana

class MpikambanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpikambana
        fields  = '__all__'

class SampanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sampana
        fields  = '__all__'