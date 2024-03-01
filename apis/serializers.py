# apis/serializers.py
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = "__all__"
        extra_kwargs = {'id': {'read_only': True}} 

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_done = validated_data.get('is_done', instance.is_done)
        instance.save()
        return instance