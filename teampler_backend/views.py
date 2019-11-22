from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from teampler_backend.models import UserData, Group
from teampler_backend.serializers import UserDataSerializer, UserDataListSerializer, GroupSerializer, GroupListSerializer

class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        serializer = UserDataListSerializer(self.queryset, many=True)
        return Response(serializer.data)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        serializer = GroupListSerializer(self.queryset, many=True)
        return Response(serializer.data)

