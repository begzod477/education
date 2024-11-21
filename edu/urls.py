from django.urls import path
from .views import StudentApiView

urlpatterns = [
    path('students/', StudentApiView.as_view(), name='students'),
    path('students/<int:pk>/', StudentApiView.as_view(), name='student-detail'),
]
