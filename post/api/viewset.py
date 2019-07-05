from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from post.models import Post
from .serializers import PostModelSerializer

class PostModelVeiwSet(ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    serializer_class = PostModelSerializer

    queryset = Post.objects.all()
    