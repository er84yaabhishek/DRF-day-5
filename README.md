# Day 5: DRF Serializer & GET API

## 1️⃣ Serializer (api/serializers.py)
```python
from rest_framework import serializers
from students.models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
✅ ModelSerializer use kiya

✅ fields="all" → saare fields serialized honge

Tip: Naming convention ke liye better hai StudentSerializer (singular).

## 2️⃣ View (api/views.py) ```python
from students.models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def studentsView(req):
    students = Student.objects.all()
    serializer = StudentSerializers(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
✅ DRF API view use kiya (@api_view)

✅ Multiple objects ke liye many=True use kiya

✅ HTTP status code 200 properly set kiya

##3️⃣ urls.py
from django.urls import path
from .views import studentsView

urlpatterns = [
    path('students/', studentsView),
]
