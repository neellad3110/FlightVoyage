from rest_framework import serializers  
from .models import User

class UserSerializer(serializers.ModelSerializer):
    name=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()

    class Meta:
        model=User

    def create(self, validated_data):
        user=User.objects.create(name=validated_data['name'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    