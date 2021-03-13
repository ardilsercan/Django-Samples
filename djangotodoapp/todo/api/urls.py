from django.urls import path
from todo.api import views as api_views


# --------------------------------    CLASS VIEWS    -------------------------------- 

urlpatterns = [
  path('todos/', api_views.TodoListCreateAPIView.as_view(), name='todo list'),
  path('todos/<int:pk>', api_views.TodoDetailAPIView.as_view(), name='todo-detail'),    
]


# --------------------------------    FUNCTION-BASED VIEWS    -------------------------------- 

# urlpatterns = [
#   path('todos/', api_views.todo_list_create_api_view, name='todo list'),
#   path('todos/<int:pk>', api_views.todo_detail_api_view, name='todo-detail'),    
# ]