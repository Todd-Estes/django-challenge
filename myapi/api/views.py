from django.shortcuts import render
from rest_framework import viewsets
from .models import Template
from .serializers import TemplateSerializer

# Create your views here.

class TemplateViewSet(viewsets.ModelViewSet):
  queryset = Template.objects.all()
  serializer_class = TemplateSerializer