from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status

# Create your views here.
def index(request):
    return JsonResponse({'message':'okay!'})

@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    todos = get_list_or_404(Todo)
    serializers = TodoSerializer(todos, many=True)
    return Response(serializers.data)

@api_view(['GET', 'DELETE'])
def todo_detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)
