from django.shortcuts import render
from .models import User, Corporation,Application
from rest_framework import viewsets
from .serializers import UserSerializer, CorporationSerializer, ApplicationSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class CorporationViewSet(viewsets.ModelViewSet):

    queryset = Corporation.objects.all()
    serializer_class = CorporationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer