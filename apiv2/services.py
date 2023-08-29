""" Module contains functions that perform non-trivial database
    operations such as write, update, and delete.
"""
from apiv2.models import Restaurant, Review
from django.http import Http404
from apiv2 import selectors
from apiv2.serializers import RestaurantSerializer, ReviewSerializer

def create_review(request):
    """ Creates a new Review record.

    Uses data within request object to create a new Review record in the database.

    Args:
        request: Request object containing the Review data to be stored.

    Returns:
        serializer: ReviewSerializer object created using request.data
    """
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return serializer

def update_review(request, pk):
    """ Updates a review record.

    Uses data within the request object to update the specified Review record.

    Args:
        request: Request object containing new data.
        pk: Integer denoting the primary key of the Review record.

    Returns:
        serializer: ReviewSerializer object with updated request.data
    """
    review = selectors.review_detail(request, pk)
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return serializer

def delete_review(request, pk):
    """ Removes a Review record.

    Deletes specified Review record from the database.

    Args:
        pk: Integer denoting the primary key of the Review record.

    Returns:
        None
    """
    review = selectors.review_detail(pk)
    review.delete()
    return
