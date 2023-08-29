from rest_framework import serializers
from apiv2.models import Restaurant, Review


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'platform_id', 'uri', 'phone_number']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['restaurant', 'reviewer', 'comment', 'platform', 'star_rating', 'menu_items']
        