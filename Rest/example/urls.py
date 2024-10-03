from django.urls import path

from example.views import hello_api, books_api, BookAPI

urlpatterns = [
    path('hello/', hello_api),
    path('fbv/books', books_api),
    path('fbv/book/<int:bid>', BookAPI.as_view())
]
