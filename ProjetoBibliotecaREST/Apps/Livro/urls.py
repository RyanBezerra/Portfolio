from django.urls import path, include
from rest_framework.routers import DefaultRouters
from .viewsets import LivroViewSet

routers = DefaultRouters()
router.register(r'livros', LivroViewSet, basename='Livro')

urlpatterns = [
    path('', include(router.urls)),
]