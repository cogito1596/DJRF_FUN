from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllStudentOperations

router = DefaultRouter()
router.register("student", AllStudentOperations)


urlpatterns = [
    path("", include(router.urls)),
]
