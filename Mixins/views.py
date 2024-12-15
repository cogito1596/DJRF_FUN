from django.shortcuts import render
from rest_framework import mixins, generics
from FBV.models import GlobalStudent
from FBV.serializers import GlobalStudentSerializer
# Create your views here.


class NonPrimaryStudentOperations(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset = GlobalStudent.objects.all()
    serializer_class = GlobalStudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PrimaryStudentOperations(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = GlobalStudent.objects.all()
    serializer_class = GlobalStudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
