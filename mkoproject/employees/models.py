from django.db import models

# Create your models here.

class Employees(models.Model):
    EmpID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    StartDate = models.DateField()
    ExitDate = models.DateField(null=True)
    Title = models.CharField(max_length=30)
    Supervisor = models.CharField(max_length=30)
    ADEmail = models.EmailField()
    EmployeeStatus = models.CharField(max_length=20)
    EmployeeType = models.CharField(max_length=20)
    PayZone = models.CharField(max_length=10)
    EmployeeClassificationType = models.CharField(max_length=20)
    TerminationType = models.CharField(max_length=20)
    TerminationDescription = models.CharField(max_length=150, null=True)
    DepartmentType = models.CharField(max_length=20)
    Division = models.CharField(max_length=20)
    DOB = models.DateField()
    State = models.CharField(max_length=10)
    JobFunctionDescription = models.CharField(max_length=20)
    GenderCode = models.CharField(max_length=10)
    LocationCode = models.IntegerField()
    RaceDesc = models.CharField(max_length=10)
    MaritalDesc = models.CharField(max_length=20)
    PerformanceScore = models.CharField(max_length=20)
    CurrentEmployeeRating = models.IntegerField()



























