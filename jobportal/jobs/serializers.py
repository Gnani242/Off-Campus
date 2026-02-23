from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "company_name",
            "location",
            "salary",
            "required_skills",
            "job_link",
            "posted_date",
        ]


class RecommendedJobSerializer(serializers.Serializer):
    job = JobSerializer()
    match_percentage = serializers.FloatField()

