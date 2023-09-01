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


def all_reviews(pk):
    """ Pulls all Review records in the database.

    Selects all Review records in the database corresponding to the Restaurant denoted
    by the pk.

    Args:
        pk: An integer denoting the desired Restaurant.
    
    Returns:
        A list of all Review records in the database for the specified Restaurant.
    """
    return Review.objects.filter(restaurant__pk=pk)

def review_detail(pk, id):
    """ Pulls a single Review record.

    Filters Review records and grabs Review that matches the specified id for the 
    restaurant denoted by pk.

    Args:
        pk: An integer denoting the Restaurant record.
        id: An integer denoting the Review record.

    Returns:
        Review: A single Review record if it exists in the database.

    Raises:
        Http404: An error occurred when searching for Review record with specified primary key.
    """
    try:
        return Review.objects.get(restaurant__pk=pk, id=id)
    except Review.DoesNotExist:
        raise Http404
