import csv from os
from django.core.management.base import BaseCommand
from employees.models import Employee

class Command(BaseCommand):
    help = 'Import employees to db from a CSV file'

    def handle(self, *args, *kwargs):
        with open('employee_data_mko.csv', newline='') as csvfile:
            content=csv.DictReader(csvfile)
            for row in content:
                Employee.objects.create(EmpID=row['EmpID'], FirstName=row['FirstName'], LastName=row['LastName'], StartDate=row['StartDate'], ExitDate=row['ExitDate'], Title=row['Title'], Supervisor=row['Supervisor'], ADEmail=row['ADEmail'], EmployeeStatus=row['EmployeeStatus'], EmployeeType=row['EmployeeType'], PayZone=row['PayZone'], EmployeeClassificationType=row['EmployeeClassificationType'], TerminationType=row['TerminationType'], TerminationDescription=row['TerminationDescription'], DepartmentType=row['DepartmentType'], Division=row['Division'], DOB=row['DOB'], State=row['State'], JobFunctionDescription=row['JobFunctionDescription'], GenderCode=row['GenderCode'], LocationCode=row['LocationCode'], RaceDesc=row['RaceDesc'], MaritalDesc=row['MaritalDesc'], PerformanceScore=row['PerformanceScore'], CurrentEmployeeRating=row['CurrentEmployeeRating'])