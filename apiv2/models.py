from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Restaurant(models.Model):
    """ Model used to store Restaurant records in our database.

    Attributes:
        name: A string denoting the name of the restaurant.
        platform_id: Optional string denoting the platforn specific identifier.
        uri: Optional string denoting the URI to the restaurant.
        phone_number: Optional string denoting the contact number of the restaurant.
    """
    name = models.CharField(max_length=50, blank=False)
    platform_id = models.CharField(max_length=50, blank=False)
    uri = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=10, default="")

    def __str__(self):
        return f"{self.id}, {self.name}, {self.platform_id}, {self.uri}, {self.phone_number}"


class Review(models.Model):
    """ Model used to store restaurant Reviews in our databse.

    The Review model has a many-to-one relationship with a restaurant. That is, a restaurant 
    has many reviews, but each review corresponds to a single restaurant.

    Attributes:
        restaurant: A foreign-key used between the review and its corresponding restaurant.
        reviewer: A string denoting the name of the customer that left the review.
        comment: A string denoting the restaurant statement made by the customer.
        platform: A string denoting the service on which the comment was made.
        star_rating: An integer denoting the restaurant stars.
        menu_items: An array denoting the items that were ordered by the customer.
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.CharField(max_length=50, blank=False)
    comment = models.TextField(blank=False)
    platform = models.CharField(max_length=50, blank=False)
    star_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    menu_items = models.JSONField()

    def __str__(self):
        return f"{self.id}, {self.restaurant}, {self.reviewer}, {self.comment}, {self.platform}, {self.star_rating}, {self.menu_items}"

