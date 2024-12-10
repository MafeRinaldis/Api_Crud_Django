from rest_framework import serializers
from .models import programmer
from .models import student

class programmerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = programmer
        fields = '_all_'

class studentSerializer (serializers.ModelSerializer):
    class Meta:
        model= student
        fields = '_all_'