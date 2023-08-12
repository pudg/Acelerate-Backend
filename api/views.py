from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Restaurant, Review
from django.core import serializers
from django.http import Http404
from common import utils
import threading


def launch_update_thread(Restaurant, Review, identifier, platform):
    thread = threading.Thread(target=utils.handle_review_refresh,
                                  args=[Restaurant, Review, identifier, platform],
                                  daemon=True)
    thread.start()
    return

def home(request):
    return redirect('/api')

def api(request):
    platforms = Review.objects.values_list('platform', flat=True).distinct()
    return render(request, 'api.html', {'platforms': platforms})

def restaurant_reviews(request, platform, identifier):
    if request.method == 'GET':
        reviews = Review.objects.filter(
            restaurant__platform_id=identifier,
            platform=platform)
        return render(request, 'restaurant_reviews.html',
                      {'reviews': reviews, 'insight': 'All'})
    elif request.method == 'POST':
        launch_update_thread(Restaurant=Restaurant, Review=Review, identifier=identifier, platform=platform)
        updated_reviews = Review.objects.filter(
            restaurant__platform_id=identifier,
            platform=platform)
        return render(request, 'restaurant_reviews.html',
                      {'reviews': updated_reviews, 'insight': 'All'})
    else:
        return HttpResponse(f"{request.method}ing...")
     
def restaurant_worst(request, platform, identifier):
    if request.method == 'GET':
        worst_reviews = Review.objects.filter(
            restaurant__platform_id=identifier,
            platform=platform,
            star_rating__lte=2)
        return render(request, 'restaurant_reviews.html',
                      {'reviews': worst_reviews, 'insight': 'Worst'})
    elif request.method == 'POST':
        launch_update_thread(Restaurant=Restaurant, Review=Review, identifier=identifier, platform=platform)
        updated_reviews = Review.objects.filter(
            restaurant__platform_id=identifier,
            platform=platform,
            star_rating__lte=2)
        return render(request, 'restaurant_reviews.html',
                      {'reviews': updated_reviews, 'insight': 'Worst'})
    else:
        return HttpResponse(f"{request.method}ing...")

def restaurant_best(request, platform, identifier):
    if request.method == 'GET':
        best_reviews = Review.objects.filter(
            restaurant__platform_id=identifier,
            platform=platform,
            star_rating__gte=5)
        return render(request, 'restaurant_reviews.html',
                      {'reviews': best_reviews, 'insight': 'Best'})
    elif request.method == 'POST':
        launch_update_thread(Restaurant=Restaurant, Review=Review, identifier=identifier, platform=platform)
        updated_reviews = Review.objects.filter(
            restaurant__platform_id=identifier,
            platform=platform,
            star_rating__gte=5)
        return render(request, 'restaurant_reviews.html',
                      {'reviews': updated_reviews, 'insight': 'Best'})
    else:
        return HttpResponse(f"{request.method}ing...")