from rest_framework.pagination import PageNumberPagination


class NewsListPagination(PageNumberPagination):
    page_size = 8
