from rest_framework import viewsets
from .models import LivroModel
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = LivroModel.objects.all()
    serializer_class = LivroSerializer