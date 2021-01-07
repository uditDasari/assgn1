from rest_framework import serializers

from app.models import Project, User, Membership


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MemShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"
