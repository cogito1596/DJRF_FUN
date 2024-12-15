from .views import NonPrimaryStudentOperations, PrimaryStudentOperations
from django.urls import path

urlpatterns = [
    path("students", NonPrimaryStudentOperations, name="FbvNon"),
    path("student/<int:pk>", PrimaryStudentOperations, name="FbvPri"),
]
