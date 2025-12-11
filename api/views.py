from django.http import JsonResponse
from students.models import Student


def studentsView(req):
    students = Student.objects.all()
    students_list = list(students.values())
    return JsonResponse(students_list,safe=False)

