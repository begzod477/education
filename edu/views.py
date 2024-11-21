from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Students, Teachers, Subjects, Grades
from .serializers import SubjectsSerializer, TeachersSerializer, GradesSerializer, StudentsSerializer
from .permissions import StudentPermission


# Create your views here.

class StudentApiView(APIView):
    serializer = StudentsSerializer
    queryset = Students.objects.all()
    permission_classes = [StudentPermission]

    def check_obj(self, request, obj):
        try:
            self.check_object_permissions(request, obj)
            return True
        except Exception:
            return False
    
    def get_perm_student(self):
        list_students = []
        students = Students.objects.all()
        for student in students:
            try:
                self.check_object_permissions(self.request, student)
                list_students.append(student)
            except:
                pass
        return list_students
    
    def get(self, request, pk=None):
        if pk:
            try:
                student = Students.objects.get(pk=pk)
                if self.check_obj(request, student):
                    serializer = self.serializer(student)
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(self.serializer(self.get_perm_student(), context = {"request": request}, many = True).data)
    
    def post(self, request, pk = None):
        if pk:
            return Response("MEthod post not allowed", status=404)
        serializer = self.serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return Response(StudentsSerializer(student))
    
    def put(self, request, pk = None):
        if not pk:
            return Response("Missing student ID", status=404)
        
        try: 
            student = Students.objects.get(pk = pk)
            serializer = self.serializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            updated_student = serializer.update(student, serializer.validated_data)

            return Response(StudentsSerializer(updated_student).data)
        except:
            return Response({"message": "student not found"},status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk=None):
        if not pk:
            return Response("Missing student ID", status=404)
        
        try:
            student = Students.objects.get(pk = pk)
            self.check_obj(request, student)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "student not found"},status=status.HTTP_404_NOT_FOUND)
    





        
