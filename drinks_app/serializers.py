from rest_framework import serializers
from .models import Drink
from .models import Recipe

class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    # drink = serializers.HyperlinkedRelatedField(
    # recipe = serializers.HyperlinkedRelatedField(
        # view_name='recipe_detail',
        # many=True,
        # read_only=True,
    # )
    class Meta:
        model = Drink
        fields = ('id', 'photo_url', 'description', 'spirit',)


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    spirit = serializers.HyperlinkedRelatedField(
        view_name='recipe_detail',
        # many=True,
        read_only=True,
    )

    class Meta:
        model = Recipe        
        fields = ('id','photo_url', 'recipe', 'name','spirit',)