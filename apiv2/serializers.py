from rest_framework import serializers
from apiv2.models import Restaurant, Review


class RestaurantSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'platform_id', 'uri', 'phone_number', 'reviews']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id', 'restaurant', 'reviewer', 'comment',
            'platform', 'star_rating', 'menu_items']
        