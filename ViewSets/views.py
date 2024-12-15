from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from FBV.models import GlobalStudent
from FBV.serializers import GlobalStudentSerializer
# Create your views here.


class AllStudentOperations(ModelViewSet):
    queryset = GlobalStudent.objects.all()
    serializer_class = GlobalStudentSerializer
