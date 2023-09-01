""" Module contains functions that perform non-trivial database
    operations such as write, update, and delete.
"""
from apiv2.models import Restaurant, Review
from django.http import Http404
from apiv2 import selectors
from apiv2.serializers import RestaurantSerializer, ReviewSerializer

def create_restaurant(request):
    """ Creates a new Restaurant record.

    Uses data within request object to create a new Restaurant record.

    Args:
        request: Request object containing Restaurant data to be stored.

    Returns:
        serializer: RestaurantSerializer object created using request.data
    """
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return serializer

def update_restaurant(request, pk):
    """ Updates a Restaurant record.

    uses data within request object to update the specified Restaurant record.

    Args:
        request: Request object containing new data.
        pk: Integer denoting the primary key of the Restaurant record.

    Returns:
        RestaurantSerializer object with updated data.
    """
    restaurant = selectors.restaurant_detail(pk=pk)
    serializer = RestaurantSerializer(restaurant, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return serializer

def delete_restaurant(pk):
    """ Removes a Restaurant record.

    Args:
        request:

        pk:
    """
    restaurant = selectors.restaurant_detail(pk=pk)
    restaurant.delete()
    return

def create_review(request):
    """ Creates a new Review record.

    Uses data within request object to create a new Review record.

    Args:
        request: Request object containing the Review data to be stored.

    Returns:
        serializer: ReviewSerializer object created using request.data
    """
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return serializer

def update_review(request, pk, id):
    """ Updates a review record.

    Uses data within the request object to update the specified Review record.

    Args:
        request: Request object containing new data.
        pk: Integer denoting the primary key of the Review record.

    Returns:
        serializer: ReviewSerializer object with updated data.
    """
    review = selectors.review_detail(pk=pk , id=id)
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return serializer

def delete_review(pk, id):
    """ Removes a Review record.

    Deletes specified Review record from the database.

    Args:
        pk: Integer denoting the primary key of the Review record.

    Returns:
        None
    """
    review = selectors.review_detail(pk=pk, id=id)
    review.delete()
    return
