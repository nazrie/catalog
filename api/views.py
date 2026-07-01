#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# View for /api/books
class BookView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"Hello": "django"})
    
book_view = BookView.as_view()