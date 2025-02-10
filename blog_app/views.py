from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Vista para todos los posts
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Vista para un solo post (detalles)
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()  # DRF maneja el filtrado por pk automáticamente
    serializer_class = PostSerializer
