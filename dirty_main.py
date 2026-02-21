from datetime import date
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    print("Текущая дата:", date.today().isoformat())
    employees = get_employees()
    calculate_salary(employees)