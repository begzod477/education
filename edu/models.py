from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Subjects(models.Model):
    name = models.CharField(max_length=55 , verbose_name='fanlar')

    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=55 , verbose_name="o'quvchilar")
    age = models.PositiveIntegerField(verbose_name="yosh", validators=[
        MinValueValidator(7),
        MaxValueValidator(77)

    ])
    adress = models.CharField(max_length=70, null=True, blank=True, verbose_name="manzil")
    subjects = models.ManyToManyField(Subjects, verbose_name="qaysi fanda oqishi", related_name="students")

    def __str__(self):
        return self.name

class Grades(models.Model):
    student = models.ForeignKey(Students, verbose_name="oquvchilar", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, verbose_name="qaysi fanga olgani", on_delete=models.CASCADE)
    grade = models.FloatField(verbose_name="oquvchi bahosi", validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.grade}"

class Teachers(models.Model):
    name = models.CharField(max_length=55 , verbose_name="oqituvchi ismi")
    subjects = models.ManyToManyField(Subjects, verbose_name="o'qituvchi qaysi fanda oqitishi", related_name="teachers")
    def __str__(self):
        return self.name
    







