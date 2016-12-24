from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Car
        fields = ('name', 'price', 'image')

