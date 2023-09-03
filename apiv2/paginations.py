from rest_framework.pagination import PageNumberPagination

MIN_PAGE_SIZE = 5
MAX_PAGE_SIZE = 50

class CustomPagination(PageNumberPagination):
    page_size = MIN_PAGE_SIZE
    page_size_query_param = 'page_size'
    max_page_size = MAX_PAGE_SIZE
    page_query_param = 'page'