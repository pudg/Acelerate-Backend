from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apiv2.serializers import RestaurantSerializer, ReviewSerializer
from apiv2 import selectors, services
from apiv2.paginations import CustomPagination
from apiv2.filters import ReviewFilter, RestaurantFilter
from django_filters.rest_framework import DjangoFilterBackend
from apiv2.paginations import MIN_PAGE_SIZE

class RestaurantList(APIView):
    """
    List all Restaurants or create a new Restaurant.
    """

    paginator = CustomPagination()
    restaurant_filter = RestaurantFilter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get(self, request, format=None):
        restaurants = selectors.all_restaurants()
        filtered_restaurants = self.restaurant_filter.filter_queryset(request=request, queryset=restaurants, view=self)
        paginated_restaurants = None
        if filtered_restaurants.exists():
            paginated_restaurants = self.paginator.paginate_queryset(filtered_restaurants, request=request)
        else:
            paginated_restaurants = self.paginator.paginate_queryset(restaurants, request=request)
        serializer = RestaurantSerializer(paginated_restaurants, many=True)
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
    
    def get(self, request, pk, format=None):
        restaurant = selectors.restaurant_detail(pk=pk)
        serializer = RestaurantSerializer(restaurant)
        if 'recently_viewed' in request.session:
            if pk in request.session['recently_viewed']:
                request.session['recently_viewed'].remove(pk)
                request.session['recently_viewed'].insert(0, pk)
            else:
                request.session['recently_viewed'].append(pk)
            if len(request.session['recently_viewed']) > MIN_PAGE_SIZE:
                    request.session['recently_viewed'].pop()
        else:
            request.session['recently_viewed'] = [pk]
        
        request.session.modified = True
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        serializer = services.update_restaurant(request, pk)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        services.delete_restaurant(pk=pk)
        return

class ReviewList(APIView):
    """
    List all Reviews or create a new Review.
    """

    paginator = CustomPagination()
    review_filter = ReviewFilter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reviewer', 'star_rating']

    def get(self, request, pk, format=None):
        reviews = selectors.all_reviews(pk=pk)
        filtered_reviews = self.review_filter.filter_queryset(request=request, queryset=reviews, view=self)
        paginated_reviews = None
        if filtered_reviews.exists():
            paginated_reviews = self.paginator.paginate_queryset(filtered_reviews, request=request)
        else:
            paginated_reviews = self.paginator.paginate_queryset(reviews, request=request)
        serializer = ReviewSerializer(paginated_reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk, format=None):
        serializer = services.create_review(request)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReviewDetail(APIView):
    """
    Retrieve, Update, or Delete a Review record.
    """

    def get(self, request, pk, id, format=None):
        review = selectors.review_detail(pk=pk, id=id)
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, id, format=None):
        serializer = services.update_review(request, pk, id)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, id, format=None):
        services.delete_review(pk=pk, id=id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    