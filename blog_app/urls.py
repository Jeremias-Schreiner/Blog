from django.urls import path
from .views import PostListCreate, PostDetail

urlpatterns = [
    path("post/", PostListCreate.as_view(), name="post-list-create"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post-detail"),
]