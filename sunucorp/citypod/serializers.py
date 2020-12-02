from rest_framework import serializers
from citypod.models import *

#serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields= '__all__'

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields= '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields= '__all__'

class PubliciteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields= '__all__'