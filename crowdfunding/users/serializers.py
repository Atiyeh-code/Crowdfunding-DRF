from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	username = serializers.CharField(max_length=200)
	email = serializers.CharField(max_length=200)
	password = serializers.CharField(write_only = True)
	first_name = serializers.CharField(max_length=30)
	last_name = serializers.CharField(max_length=100)
	image = serializers.URLField(max_length=200)
	location = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return CustomUser.objects.create_user(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):
	def update(self, instance, validated_data):
	    instance.username = validated_data.get('user name', instance.username)
	    instance.first_name = validated_data.get('first name', instance.first_name)
	    instance.last_name = validated_data.get('last name', instance.last_name)
	    instance.image = validated_data.get('image', instance.image)
	    instance.location = validated_data.get('location', instance.location)
	    instance.save()
	    return instance

