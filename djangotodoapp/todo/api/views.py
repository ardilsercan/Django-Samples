from rest_framework import status # HTTP 200 etc.
from rest_framework.response import Response # redirect or render structures
from rest_framework.decorators import api_view


from todo.models import Todo
from todo.api.serializers import TodoSerializer

# --------------------------------    CLASS VIEWS    -------------------------------- 
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class TodoListCreateAPIView(APIView):
    def get(self, request): 
        todos = Todo.objects.filter(completed=True) 
        serializer = TodoSerializer(todos, many=True) 
        return Response(serializer.data)


    def post(self, request):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED) 
        return Response(status = status.HTTP_400_BAD_REQUEST)


class TodoDetailAPIView(APIView):

    def get_object(self, pk):
        todo_instance = get_object_or_404(Todo, pk=pk)
        return todo_instance

    def get(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = TodoSerializer(todo, data = request.data) 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 




# --------------------------------    FUNCTION-BASED VIEWS    -------------------------------- 
# @api_view(['GET', 'POST']) # JSONrenderer gibi işlemlere gerek yok, arka tarafta api_view ile handle ediliyor.
# def todo_list_create_api_view(request):
    
#     if request.method == 'GET':
#         todos = Todo.objects.filter(completed=True) # Normalde burda Query Set döner, fakat serializer da tek bir nesne mantığı var.
#         serializer = TodoSerializer(todos, many=True) # many=True query set response sonrası alınan hata için eklendi.
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TodoSerializer(data = request.data) # gönderilen data serialize edildi.
#         if serializer.is_valid(): #Gelen data doğru mu kontrolü yapılır.
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED) # HTTP 201 mesajı status ile gönderilir.
#         return Response(status = status.HTTP_400_BAD_REQUEST) #NOT: if koşulundan sonra zaten serializer valid değilse direkt bu satır çalışır.

# @api_view(['GET', 'PUT', 'DELETE'])
# def todo_detail_api_view(request, pk):
#     try:
#         todo_instance = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(
#             {
#                 'errors': {
#                     'code': 404,
#                     'message': 'Boyle bir id {{pk}}ile todo bulunamadı.'
#                 }
#             },    
#             status = status.HTTP_404_NOT_FOUND
#         )

#     if request.method == 'GET':
#         serializer = TodoSerializer(todo_instance) #many=True'ya gerek kalmadı çünkü artık tek bir instance verildi.
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TodoSerializer(todo_instance, data = request.data) 
#         if serializer.is_valid(): 
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status = status.HTTP_400_BAD_REQUEST)
    
#     elif request.method =='DELETE':
#         todo_instance.delete()
#         return Response(
#             {
#                 'işlem': {

#                     'code': 204,
#                     'message': f'({pk}) id numaralı todo silinmiştir.'
#                 }
#             },
#             status = status.HTTP_204_NO_CONTENT
#         )



