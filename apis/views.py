from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'deleted': True})