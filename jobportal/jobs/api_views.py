from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Job
from .serializers import JobSerializer, RecommendedJobSerializer
from .services import get_recommended_jobs_for_user


class JobListAPI(generics.ListAPIView):
    """
    GET /api/jobs/?search=&location=&limit=
    """

    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Job.objects.order_by("-posted_date")
        search = self.request.query_params.get("search")
        location = self.request.query_params.get("location")
        if search:
            qs = qs.filter(title__icontains=search)
        if location:
            qs = qs.filter(location__icontains=location)

        limit = self.request.query_params.get("limit")
        if limit and limit.isdigit():
            return qs[: int(limit)]
        return qs


class RecommendedJobsAPI(APIView):
    """
    GET /api/recommended-jobs/
    Requires authenticated user.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pairs = get_recommended_jobs_for_user(request.user)
        data = [
            {"job": JobSerializer(job).data, "match_percentage": match}
            for job, match in pairs
        ]
        serializer = RecommendedJobSerializer(data, many=True)
        return Response(serializer.data)

