from rest_framework.pagination import PageNumberPagination


class NotaryListPagination(PageNumberPagination):
    page_size = 3
