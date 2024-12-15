from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from FBV.models import GlobalStudent
from FBV.serializers import GlobalStudentSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class NonPrimaryStudentOperations(APIView):
    def get(self, request):
        students = GlobalStudent.objects.all()
        serializer = GlobalStudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GlobalStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class PrimaryStudentOperations(APIView):
    def get_object(self, pk):
        return get_object_or_404(GlobalStudent, pk=pk)

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = GlobalStudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = GlobalStudentSerializer(student, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
