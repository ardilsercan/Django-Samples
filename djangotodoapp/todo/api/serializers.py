from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    completed = serializers.BooleanField()

    def create(self, validated_data):
        print(validated_data)
        return Todo.objects.create(**validated_data) # ** kullanılmalı, dictionary geldiği için hata alır.

    def update(self, instance, validated_data):
        instance.title= validated_data.get('title', instance.title)
        instance.completed= validated_data.get('completed', instance.completed)
        instance.save()
        return instance