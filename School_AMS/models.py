from django.db import models

# Create your models here.
class Student (models.Model):
    student_id = models.PositiveIntegerField(primary_key= True)
    f_name = models.CharField(max_length=100,)
    l_name = models.CharField(max_length=100,)
    student_email = models.EmailField(max_length=50, unique=True)
    course = models.CharField(max_length=100,)
    student_year = models.IntegerField()

    def __str__(self):
        return f'Student: {self.student_id} {self.f_name} {self.l_name} {self.student_email} {self.course} {self.student_year}'


class Faculty (models.Model):
    faculty_name = models.CharField(max_length=100,)
    subject = models.CharField(max_length=50, unique=True)
    enrolled= models.CharField(max_length=100)
    session = models.IntegerField()
    

    def __str__(self):
        return f'Faculty: {self.faculty_name} {self.subject} {self.enrolled} {self.session}'

class Finance (models.Model):
    student_acc = models.IntegerField(primary_key=True)
    adm_no = models.ForeignKey(Student, on_delete=models.RESTRICT)
    amount = models.IntegerField()
    date = models.DateField(max_length=50)
    
    def __str__(self):
        return f'Finance: {self.student_acc} {self.adm_no} {self.amount} {self.date}'






