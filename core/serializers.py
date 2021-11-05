from django.db.models import fields
from .models import *
from rest_framework import serializers

class PosturaTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaPostura
        fields = '__all__'