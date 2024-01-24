import csv 
from django.core.management.base import BaseCommand
from employees.models import Employees
MONTH = {'Jan':'01', 'Feb':'02', 'mar':'03', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

class Command(BaseCommand):
    help = 'Import employees to db from a CSV file'

    def handle(self, *args, **kwargs):
        with open('employee_data_mko.csv', newline='') as csvfile:
            content=csv.DictReader(csvfile)
            for row in content:
                if(row['StartDate']):
                    for key in MONTH:
                        row['StartDate']=row['StartDate'].replace(key,MONTH[key]).replace('.', '-')
                    buffer = row['StartDate'].split(sep='-')
                    row['StartDate'] = buffer[0] + '-' + buffer[1] + '-' + '20' + buffer[2]
                    print(row['StartDate'])

                    
                    
                    
                # Employees.objects.create(EmpID=row['EmpID'], FirstName=row['FirstName'], LastName=row['LastName'], StartDate=row['StartDate'], ExitDate=row['ExitDate'], Title=row['Title'], Supervisor=row['Supervisor'], ADEmail=row['ADEmail'], EmployeeStatus=row['EmployeeStatus'], EmployeeType=row['EmployeeType'], PayZone=row['PayZone'], EmployeeClassificationType=row['EmployeeClassificationType'], TerminationType=row['TerminationType'], TerminationDescription=row['TerminationDescription'], DepartmentType=row['DepartmentType'], Division=row['Division'], DOB=row['DOB'], State=row['State'], JobFunctionDescription=row['JobFunctionDescription'], GenderCode=row['GenderCode'], LocationCode=row['LocationCode'], RaceDesc=row['RaceDesc'], MaritalDesc=row['MaritalDesc'], PerformanceScore=row['PerformanceScore'], CurrentEmployeeRating=row['CurrentEmployeeRating'])