from rest_framework import serializers
from .models import GlobalStudent


class GlobalStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalStudent
        fields = "__all__"
