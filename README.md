Django + DRF Setup Steps (Day Summary)

1.  GitHub se project clone kiya: git clone

2.  Virtual environment setup: python -m venv venv venv

3.  Django + DRF install: pip install django djangorestframework

4.  Project URLs setup:

    -   admin/
    -   students/ (web endpoint)
    -   app/v1/ (API endpoint)

5.  Students app view (web): def students(): return HttpResponse(student
    list)

6.  Student model create kiya.

7.  Admin me Student model register: admin.site.register(Student)

8.  Students app URL setup.

9.  API app JSON endpoint banaya: JsonResponse return kiya.

10. API URLs setup.

11. Migrations flow: python manage.py makemigrations python manage.py
    migrate

12. Admin user create: python manage.py createsuperuser
=======================================================================
1. GitHub se Project Clone Kiya
git clone <repo-link>
2. Virtual Environment Setup Kiya
   python -m venv venv
venv\Scripts\activate
3. Required Packages Install Kiye
pip install django djangorestframework
4. Django Project URLs Setup
   
                            from django.contrib import admin
                            from django.urls import path, include
                            
                            urlpatterns = [
                                path('admin/', admin.site.urls),
                            
                                # Web Application
                                path('students/', include('students.urls')),
                            
                                # API Endpoints
                                path('app/v1/', include('api.urls')),
                            ]
6. Students App — View for Web
                              from django.http import HttpResponse
                              
                              def students(req):
                                  students = [
                                      {'id':1 , 'name':'Abhishek','age':25}
                                  ]
                                  return HttpResponse(students)
6. Students Model Created
                            class Student(models.Model):
                                student_id = models.CharField(max_length=50) 
                                name = models.CharField(max_length=50)
                                branch = models.CharField(max_length=50)
                            
                                def __str__(self):
                                    return self.name
7. Admin Panel Me Model Register Kiya
                                from django.contrib import admin
                              from .models import Student

                              admin.site.register(Student)
8. Students URLs Setup
                              from django.urls import path
                              from . import views
                              
                              urlpatterns = [
                                  path('', views.students),
                              ]
9. API App — JSON Endpoint Created
                              from django.http import JsonResponse
                              
                              def studentView(req):
                                  students = {
                                      'id': 1,
                                      'name': 'Abhishek',
                                      'class': 'cs'
                                  }
                                  return JsonResponse(students)
10. API URLs Setup
                                from django.urls import path
                                from . import views
                                
                                urlpatterns = [
                                    path('students/', views.studentView),
                                ]
11. Migrations Flow
                              python manage.py makemigrations
                              python manage.py migrate
12. Admin User Create Kiya

                              python manage.py createsuperuser

























































































