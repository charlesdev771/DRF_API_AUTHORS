from rest_framework import serializers
from core.models import Authors


class AuthorsSerializer(serializers.ModelSerializer):
    
    class Meta:
    
        model = Authors
        fields = ['id', 'name', 'age']