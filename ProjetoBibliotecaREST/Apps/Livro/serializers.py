from rest_framework import serializers
from .models import LivroModel

"""criação do serializers da model Livro"""

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivroModel
        fields = '__all__'