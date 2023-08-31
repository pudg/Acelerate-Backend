from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apiv2.serializers import RestaurantSerializer, ReviewSerializer
from apiv2 import selectors, services

class RestaurantList(APIView):
    """
    List all Restaurants or create a new Restaurant.
    """
    def get(self, request, format=None):
        restaurants = selectors.all_restaurants()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = services.create_restaurant(request=request)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetail(APIView):
    """
    Retrieve, Update, or Delete a Restaurant Record.
    """
    serializer_class = RestaurantSerializer
    def get(self, request, pk):
        restaurant = selectors.restaurant_detail(pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        serializer = services.create_restaurant(request, pk)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        services.delete_restaurant(pk=pk)
        return

class ReviewList(APIView):
    """
    List all Reviews or create a new Review.
    """
    def get(self, request, format=None):
        reviews = selectors.all_reviews()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = services.create_review(request)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReviewDetail(APIView):
    """
    Retrieve, Update, or Delete a Review record.
    """
    serializer_class = ReviewSerializer

    def get(self, request, pk):
        review = selectors.review_detail(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        serializer = services.update_review(request, pk)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        services.delete_review(pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
    