from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Restaurant(models.Model):
    """ Model used to store Restaurant records in our database.

    Attributes:
        name: A string denoting the name of the restaurant.
        address: Optional string denoting the street address of the restaurant.
        phone_number: Optional string denoting the contact number of the restaurant.
    """
    name = models.CharField(max_length=50)
    platform_id = models.CharField(max_length=50, default=0)
    uri = models.CharField(max_length=100, blank=False, default="")
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.name}, {self.uri}, {self.platform_id}"
    class Meta:
        ordering = ["name"]


class Review(models.Model):
    """ Model used to store restaurant Reviews in our databse.

    The Review model has a many-to-one relationship with a restaurant. That is, a restaurant 
    has many reviews, but each review corresponds to a single restaurant.

    Attributes:
        restaurant: A foreign-key used between the review and its corresponding restaurant.
        reviewer: A string denoting the name of the customer that left the review.
        comment: A string denoting the restaurant statement made by the customer.
        platform: A string denoting the service on which the comment was made.
        rating: An integer denoting the restaurant stars.
        menu_items: An array denoting the items that were ordered by the customer.
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=50)
    comment = models.TextField()
    platform = models.TextField(max_length=50, blank=False)
    star_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    menu_items = models.JSONField()

    def __str__(self):
        return f"{self.reviewer}, {self.comment}, {self.platform}, {self.star_rating}, {self.menu_items}"