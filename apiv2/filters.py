from django_filters.rest_framework import DjangoFilterBackend

class ReviewFilter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filterset_class(view, queryset=queryset)
        if filter_class:
            return filter_class(request.query_params, queryset=queryset, request=request).qs
        return queryset


class RestaurantFilter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filterset_class(view, queryset=queryset)
        if filter_class:
            return filter_class(request.query_params, queryset=queryset, request=request).qs
        return queryset