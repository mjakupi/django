from rest_framework import serializers
from .models import Team
from  cities .models import Town

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        # fields  = ('name','league')
        fields = '__all__'


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
         model = Town
         # fields = (model.name)
         fields = '__all__'
