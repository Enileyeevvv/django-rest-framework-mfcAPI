from django.db.models import Q
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from django.shortcuts import render, redirect
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Service
from .models import Category

from .serializers import ServiceSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    @action(methods = ['get'], detail = False)
    def category(self, request):
        category = Category.objects.all()
        return Response({'category': [c.name for c in category]})

    @action(methods = ['post'], detail = True)
    def post_category(self, request):
        category = Category.objects.all()
        return Response({'category': [c.name for c in category]})

class FilterServicesByQ(ModelViewSet):
    queryset = Service.objects.filter((Q(category=1))|(Q(category=3))|(Q(category=5)))
    serializer_class = ServiceSerializer

class FilterServicesBySearch(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


def redirect_view(request):
    response = redirect('api/services/')

    return response