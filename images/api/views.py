from rest_framework import viewsets
from .serializers import ImageSerializer
from ..models import Image


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer