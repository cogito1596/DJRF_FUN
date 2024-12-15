from django.shortcuts import render
from FBV.models import GlobalStudent
from FBV.serializers import GlobalStudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class NonPrimaryStudentOperations(ListCreateAPIView):
    queryset = GlobalStudent.objects.all()
    serializer_class = GlobalStudentSerializer


class PrimaryStudentOperations(RetrieveUpdateDestroyAPIView):
    queryset = GlobalStudent.objects.all()
    serializer_class = GlobalStudentSerializer
