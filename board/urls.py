from django.urls import path
from rest_framework import routers
from .views import PostViewSet, CommentCreateAPIView, CommentRetrieveUpdateDestroyAPIView, like_or_dislike_post

router = routers.SimpleRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('post/<int:pk>/comment/', CommentCreateAPIView.as_view()),
    path('post/<int:pk>/like/', like_or_dislike_post),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
]

urlpatterns += router.urls
