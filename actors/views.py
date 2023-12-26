from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from actors.models import Actor
from actors.serializers import ActorSerializer

class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer