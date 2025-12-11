from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def students(req):
    students = [
        {'id':1 , 'name':'Abhishek','age':25}
    ]
    return HttpResponse(students)