from rest_framework import serializers
from .models import User, Events

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "name", "email", "password")

# Event serializer
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("pk", "event_name", "date", "time", "location", "image", "is_liked")
