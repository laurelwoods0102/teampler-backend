from rest_framework import serializers

from teampler_backend.models import UserData, Group

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

class UserDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['pk', 'name']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['pk', 'title']
