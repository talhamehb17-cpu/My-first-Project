from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 11  # default size
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'success': True,
            'message': "Paginated data fetched successfully",
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'data': data,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'previous': self.get_previous_link()
        })
