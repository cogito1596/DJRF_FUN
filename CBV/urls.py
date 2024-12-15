from django.urls import path
from .views import NonPrimaryStudentOperations, PrimaryStudentOperations

urlpatterns = [
    path("students", NonPrimaryStudentOperations.as_view(), name="CbvNon"),
    path("student/<int:pk>", PrimaryStudentOperations.as_view(), name="CbvPri"),
]
