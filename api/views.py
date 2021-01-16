from .serializers import VideoSerializer
from .models import Video
from rest_framework import viewsets


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

