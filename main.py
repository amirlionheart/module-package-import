from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    # вывод текущей даты
    print("Текущая дата:", date.today().isoformat())

    # вызываем функции из модулей
    employees = get_employees()
    calculate_salary(employees)

if __name__ == '__main__':
    main()