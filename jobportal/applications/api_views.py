from rest_framework import generics, permissions

from .models import Application
from .serializers import ApplicationSerializer


class ApplicationListCreateAPI(generics.ListCreateAPIView):
    """
    GET /api/applications/
    POST /api/applications/
    """

    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            Application.objects.select_related("job")
            .filter(user=self.request.user)
            .order_by("-applied_date")
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

