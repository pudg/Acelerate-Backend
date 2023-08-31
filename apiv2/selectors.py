""" Module contains functions that perform database filtering operations
    such as getting all or filtering for a specific object.
"""

from apiv2.models import Restaurant, Review
from django.http import Http404

def all_restaurants():
    """ Pulls all Restaurant records in the database.

    Returns:
        A list of all Restaurant records in the database.
    """
    return Restaurant.objects.all()

def restaurant_detail(pk):
    """ Pulls a single Restaurant record.

    Filteres Restaurant records and grabs Restaurant that matches the specified primary key.

    Args:
        pk: An integer denoting the Restaurant record primary key.

    Returns:
        Restaurant: A single Restaurant record if it exists in the database.

    Raise:
        Http404: An error occurred when searching for Restaurant record with specified primary key.
    """
    try:
        return Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        raise Http404


def all_reviews():
    """ Pulls all Review records in the database.
    
    Returns:
        A list of all Review records in the database.
    """
    return Review.objects.all()

def review_detail(pk):
    """ Pulls a single Review record.

    Filters Review records and grabs Review that matches the specified primary key.

    Args:
        pk: An integer denoting the Review record primary key.

    Returns:
        Review: A single Review record if it exists in the database.

    Raises:
        Http404: An error occurred when searching for Review record with specified primary key.
    """
    try:
        return Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        raise Http404
