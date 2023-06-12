from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Topic
from .serializers import TopicSerializer   # TODO: update to TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()  # TODO: query only logged in user Topics
    serializer_class = TopicSerializer