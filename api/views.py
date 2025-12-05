from django.shortcuts import render
from .models import Mpikambana, Sampana
from rest_framework import viewsets
from .serializers import MpikambanaSerializer, SampanaSerializer



class ViewMpikambana(viewsets.ModelViewSet):
    queryset = Mpikambana.objects.all()
    serializer_class = MpikambanaSerializer

class ViewSampana(viewsets.ModelViewSet):
    queryset = Sampana.objects.all()
    serializer_class = SampanaSerializer
    
