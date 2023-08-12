from django.core.management.base import BaseCommand, CommandError, CommandParser
from api.models import Review, Restaurant
from api.views import launch_update_thread

class Command(BaseCommand):
    help = "Updates all reviews for the available restaurants."
    def add_arguments(self, parser):
        parser.add_argument("all", nargs="+", type=str)

    def handle(self, *args, **options):
        restaurant_ids = Restaurant.objects.values_list('platform_id', flat=True)
        restaurant_ids = list(restaurant_ids)
        for restaurant_id in restaurant_ids:
            try:
                restaurant = Restaurant.objects.filter(platform_id=restaurant_id)
                launch_update_thread(Restaurant=Restaurant,
                                     Review=Review,
                                     identifier=restaurant_id,
                                     platform="grubhub")
            except Review.DoesNotExist:
                raise CommandError(f"Restaurant: {restaurant_id} does not exist.")
            
            self.stdout.write(
                self.style.SUCCESS(f"Sucessfully updated restaurant: {restaurant_id}")
            )