from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    # songs = serializers.HyperlinkedRelatedField(
    #     view_name='song_detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = Drink
        fields = ('id', 'photo_url', 'description', 'spirit',)