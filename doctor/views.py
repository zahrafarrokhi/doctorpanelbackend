from django.shortcuts import render
from rest_framework import viewsets, mixins
# Create your views here.
from doctor.models import Doctor
from doctor.serializers import DoctorSerializer


class DoctorsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DoctorSerializer
    permission_classes = []

    def get_queryset(self):
        return Doctor.objects.all()