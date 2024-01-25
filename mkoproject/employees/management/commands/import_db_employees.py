import csv 
from django.core.management.base import BaseCommand
from employees.models import Employees
MONTH = {'Jan':'01', 'Feb':'02', 'mar':'03', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

def fix_date(date_string):
    for key in MONTH:
        date_string=date_string.replace(key,MONTH[key])
    date_string=date_string.replace('.', '-')
    buffer = date_string.split(sep='-')
    if(len(buffer[2])==2):
        date_string = '20' + buffer[2] +  '-' + buffer[1] + '-' + buffer[0] 
    else:
        date_string = buffer[2] +  '-' + buffer[1] + '-' + buffer[0]
    return date_string

class Command(BaseCommand):
    help = 'Import employees to db from a CSV file'

    def handle(self, *args, **kwargs):
        with open('employee_data_mko.csv', newline='') as csvfile:
            content=csv.DictReader(csvfile)
            for row in content:
                if row['StartDate']:
                    row['StartDate']=fix_date(row['StartDate'])
                if len(row['ExitDate'])>0:
                    row['ExitDate']=fix_date(row['ExitDate'])
                else:
                    row['ExitDate'] = None
                if row['DOB']:
                    row['DOB']=fix_date(row['DOB'])
                Employees.objects.create(EmpID=row['EmpID'], FirstName=row['FirstName'], LastName=row['LastName'], StartDate=row['StartDate'], ExitDate=row['ExitDate'], Title=row['Title'], Supervisor=row['Supervisor'], ADEmail=row['ADEmail'], EmployeeStatus=row['EmployeeStatus'], EmployeeType=row['EmployeeType'], PayZone=row['PayZone'], EmployeeClassificationType=row['EmployeeClassificationType'], TerminationType=row['TerminationType'], TerminationDescription=row['TerminationDescription'], DepartmentType=row['DepartmentType'], Division=row['Division'], DOB=row['DOB'], State=row['State'], JobFunctionDescription=row['JobFunctionDescription'], GenderCode=row['GenderCode'], LocationCode=row['LocationCode'], RaceDesc=row['RaceDesc'], MaritalDesc=row['MaritalDesc'], PerformanceScore=row['PerformanceScore'], CurrentEmployeeRating=row['CurrentEmployeeRating'])


# to run this script: python manage.py import_db_employees