from django.db import models

# Create your models here.


class School(models.Model):
    name=models.CharField(max_length=100,unique=True)
    phone_number=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    #student_id = models.AutoField(primary_key=True,null=True)
    first_name=models.CharField(max_length=100,unique=True)
    last_name=models.CharField(max_length=100,null=True,blank=True,unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE,blank=True,null=True)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True,null=True)
    mail=models.EmailField(max_length = 100,blank=True,null=True)
    books=models.ManyToManyField(Book,blank=True)
    no_of_pages_read=models.IntegerField(blank=True,null=True)
    raw_id_fields = ("books",)
    def __str__(self):
        if self.last_name:
            return self.first_name+" "+self.last_name
        else:
            return self.first_name


