from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):

    photo = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Person
        fields = ('name','lname','photo')


