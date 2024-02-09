# apis/serializers.py
from rest_framework import serializers
from todo import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "title",
            "description",
            "is_done",
            "created_at",
            "updated_at",
            )
        model = models.Todo
