from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsSelfOrAdminUser
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSelfOrAdminUser]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]



