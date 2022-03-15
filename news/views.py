from rest_framework import generics
from news.serializers import *
from rest_condition import And, Or
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from register.permissions import *


class NewsImageListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = NewsImage.objects.all()
    serializer_class = NewsImageSerializer


class NewsImageListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = NewsImage.objects.all()
    serializer_class = NewsImageIdSerializer


class NewsImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = NewsImage.objects.all()
    serializer_class = NewsImageSerializer


class NewsEventListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = NewsEvent.objects.all()
    serializer_class = NewsEventSerializer


class NewsEventListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = NewsEvent.objects.all()
    serializer_class = NewsEventIdSerializer


class NewsEventDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = NewsEvent.objects.all()
    serializer_class = NewsEventSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isPatient, isNurse, isDoctor, isReceptionist)]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Comment.objects.all()
    serializer_class = CommentIdSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReactionListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isPatient, isNurse, isDoctor, isReceptionist)]
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


class ReactionListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Reaction.objects.all()
    serializer_class = ReactionIdSerializer


class ReactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


class ShareOnListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isPatient, isNurse, isDoctor, isReceptionist)]
    queryset = ShareOn.objects.all()
    serializer_class = ShareOnSerializer


class ShareOnListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = ShareOn.objects.all()
    serializer_class = ShareOnIdSerializer


class ShareOnDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = ShareOn.objects.all()
    serializer_class = ShareOnSerializer


