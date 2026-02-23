from rest_framework import generics, permissions

from .models import User
from .serializers import UserProfileSerializer


class ProfileAPI(generics.RetrieveUpdateAPIView):
    """
    GET /api/profile/
    PATCH /api/profile/
    """

    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> User:
        return self.request.user

