from rest_framework import serializers

class SampleSerializer(serializers.Serializer):
    id = serializers.CharField()

class SimpleUserSerializer(serializers.Serializer):
    pass

class SimpleUserAddSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
