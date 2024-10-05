from django.urls import path

from mytodo.views import TodosAPIView, TodoApiView, DoneTodoApiView, DoneTodosAPIView

urlpatterns = [
    path('todo/', TodosAPIView.as_view(), name='todos'),
    path('todo/<int:pk>/', TodoApiView.as_view(), name='todoDetail'),
    path('done/', DoneTodosAPIView.as_view(), name='dones'),
    path('done/<int:pk>/', DoneTodoApiView.as_view(), name='doneComplete'),
]
