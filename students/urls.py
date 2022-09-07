from django.urls import path
from .views import AddStudentView,AddBookView,AddSchoolView,SearchStudentView,ListStudentView,SearchStudentView

urlpatterns = [
    path('', SearchStudentView,name="home"),
     path('student/add', AddStudentView,name="add_student"),
     path('book/add', AddBookView,name="add_book"),
     path('school/add', AddSchoolView,name="add_school"),
     path('student/<int:pk>', ListStudentView, name='student_detail'),
]