
from .models import Archive
from .serializers import ArchiveSerializer

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class ArchiveViewSet(ModelViewSet):
    queryset = Archive.objects.all()
    
    serializer_class = ArchiveSerializer
    
    parser_classes = (MultiPartParser, FormParser)
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]