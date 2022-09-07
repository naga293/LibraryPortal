# Create your views here.
from django.shortcuts import render
import requests
from .forms import AddStudentForm, AddBookForm,AddSchoolForm,SearchStudentForm
from django.contrib import messages
from .models import School,Student,Book
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import redirect
from django.http import Http404

@csrf_exempt
def AddStudentView(request):
    if request.method=="POST":
        form = AddStudentForm(request.POST)
        if form.is_valid():
            try:   
                form.save()
                messages.success(request, 'Student added successfully')
            except Exception as e:
                messages.error(request, e)
        else:
            messages.error(request, form.errors)
    form=AddStudentForm()
    return render(request, 'student.html', {'form': form})

@csrf_exempt
def AddBookView(request):
    try:
        
        if request.method=="POST":
            form = AddBookForm(request.POST)
            if form.is_valid(): 
                try:  
                    print("RUn")
                    form.save()
                    messages.success(request, 'Book added successfully')
                except Exception as e:
                    messages.error(request, e)
            else:
                messages.error(request, form.errors)
    except Exception as e:
        messages.error(request, e)
    form=AddBookForm()
    return render(request, 'book.html', {'form': form})

@csrf_exempt
def AddSchoolView(request):
    try:
        if request.method=="POST":
            form = AddSchoolForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, 'School added successfully')
                except Exception as e:
                    messages.error(request, e)
            else:
                messages.error(request, form.errors)
    except Exception as e:
        messages.error(request, e)
    
    form=AddSchoolForm()
    return render(request, 'school.html', {'form': form})

@csrf_exempt
def ListStudentView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        messages.error(request, 'Student does not exit')


    return render(request, 'student_detail.html', context={'student': student})

@csrf_exempt
def SearchStudentView(request):
    try:
        if request.method=="POST":
            form = SearchStudentForm(request.POST)
            if form.is_valid():   
                input_type=request.POST.get("input_type")
                input=request.POST.get("input")
                if input_type=="ID":
                    try:
                        pk=int(input)
                        return redirect('student_detail',pk=pk)
                    except Exception as e:
                        messages.error(request, e)
                else:
                    name=input.split(" ")
                    if len(name)>1:
                        try:
                            student = Student.objects.get(first_name=name[0],last_name=name[1])
                            pk=student.pk
                            return redirect('student_detail',pk=pk)
                        except Student.DoesNotExist:
                            messages.error(request, 'Student does not exit')
                    else:
                        try:
                            if Student.objects.filter(first_name=name[0]).exists():
                                student = Student.objects.get(first_name=name[0])
                                pk=student.pk
                            else:
                                student = Student.objects.get(last_name=name[0])
                                pk=student.pk
                            return redirect('student_detail',pk=pk)
                        except Student.DoesNotExist:
                            messages.error(request, 'Student does not exit') 
            else:
                messages.error(request, form.errors)
    except Exception as e:
        messages.error(request, e)                       
            
    form=SearchStudentForm()
    return render(request, 'Home.html',{"form":form})