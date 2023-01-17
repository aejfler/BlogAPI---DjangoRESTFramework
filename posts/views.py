from rest_framework import generics, permissions
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class PostListView(generics.ListCreateAPIView):
    """ following line: (permission_classes = (permissions.IsAuthenticated,)
    can be used when we specify permission on a view level otherwise we can set project-level permission in settings """
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


