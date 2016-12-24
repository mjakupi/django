from rest_framework import serializers
from .models import Town

class CitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        #fields = (model.name)
        fields = '__all__'
