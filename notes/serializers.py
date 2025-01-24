from rest_framework import serializers
from .models import Notes, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    
class NotesSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source="sender.username", read_only=True)
    receiver_username = serializers.CharField(source="sender.username", read_only=True)
    
    class Meta:
        model = Notes
        fields = ["id", "sender", "receiver", "message", "timestamp", "sender_username", "receiver_username"]
        extra_kwargs = {'sender': {"write_only": True}, 'receiver': {"write_only": True}}