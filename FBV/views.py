from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import GlobalStudent
from .serializers import GlobalStudentSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


@api_view(["GET", "POST"])
def NonPrimaryStudentOperations(request):
    students = GlobalStudent.objects.all()
    if request.method == "GET":
        serializer = GlobalStudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = GlobalStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def PrimaryStudentOperations(request, pk):
    student = GlobalStudent.objects.get(pk=pk)
    if request.method == "GET":
        serializer = GlobalStudentSerializer(student)
        return Response(serializer.data, status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = GlobalStudentSerializer(student, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.error, status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
