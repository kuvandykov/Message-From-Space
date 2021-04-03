from rest_framework import serializers
from .models import MessageFromSpace


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MessageFromSpace
        fields = ['id', 'date', 'text', 'read']

