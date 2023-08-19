from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.TodoListView.as_view(), name="td_list"),
    # path("list/<int:pk>", views.TodoDetailView.as_view(), name="td_detail"),
    path("list/<int:pk>/edit", views.TodoUpdateView.as_view(), name="td_edit"),
    path("list/<int:pk>/delete", views.TodoDeleteView.as_view(), name="td_delete"),
    path("list/new", views.TodoCreateView.as_view(), name="td_new"),
]