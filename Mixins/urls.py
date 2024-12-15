from django.urls import path
from .views import NonPrimaryStudentOperations, PrimaryStudentOperations

urlpatterns = [
    path("students", NonPrimaryStudentOperations.as_view(), name="MixNon"),
    path("student/<int:pk>", PrimaryStudentOperations.as_view(), name="MixPri"),
]
