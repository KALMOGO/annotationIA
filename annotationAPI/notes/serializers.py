from rest_framework import serializers
from .models import *

class AudioSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Audio
        fields = '__all__'


