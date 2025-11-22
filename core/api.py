from rest_framework import viewsets, filters
from .models import CustomModel
from .serializers import CustomModelSerializer
from .permissions import IsStaffOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CustomModelViewSet(viewsets.ModelViewSet):
    queryset = CustomModel.objects.all().order_by('-created')
    serializer_class = CustomModelSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['created']
    search_fields = ['title', 'description']
