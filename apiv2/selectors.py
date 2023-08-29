""" Module contains functions that perform database filtering operations
    such as getting all or filtering for a specific object.
"""

from apiv2.models import Restaurant, Review
from django.http import Http404


def all_reviews():
    """ Pulls all Review records in the database.
    
    Returns:
        A list of all Review records in the database.
    """
    reviews = Review.objects.all()
    return reviews

def review_detail(pk):
    """ Pulls a single Review record.

    Filters Review records and grabs Review that matches the specified primary key.

    Args:
        pk: An integer denoting the Review record primary key.

    Returns:
        A single Review record if it exists in the database.

    Raises:
        Http404: An error occurred when searching for Review record with specified primary key.
    """
    try:
        return Review.objects.filter(pk=pk)
    except Review.DoesNotExist:
        raise Http404
