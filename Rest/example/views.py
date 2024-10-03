from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from example.models import Book
from example.serializer import BookSerializer


# Create your views here.
@api_view(['GET'])
def hello_api(request: Request):
    return Response({'hello': 'world'})


# functional view
@api_view(['GET', 'POST'])
def books_api(request: Request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class view
class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, id=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
