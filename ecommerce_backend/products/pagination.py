from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10                  # items per page default
    page_size_query_param = 'page_size'  # allow user to override size
    max_page_size = 100