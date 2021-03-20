from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'  # GET all data
        # fields = ['title', 'completed'] # GET only title and completed value
        #exclude = ['title']
        read_only_fields = ['id']



# -------------- STANDARD SERIALIZER -------------- #

class TodoDefaultSerializer(serializers.Serializer):
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

# -------------- STANDARD SERIALIZER -------------- #

     # -------------- VALIDATION -------------- # 

    def validate(self, data): #object seviyesinde
        if data['title'] == data['completed']:
            raise serializers.ValidationError('Baslik ve durum alanları aynı olamaz. Lütfen farklı bir başlık giriniz.')
        return data

    def validate_title(self, value): #value seviyesinde
        if len(value) < 4:
          raise serializers.ValidationError(f'Başlık alanı 4 karakterden az olamaz. Giriş yapılan karakter sayısı: {len(value)}')
        return value 

    # -------------- VALIDATION -------------- # 