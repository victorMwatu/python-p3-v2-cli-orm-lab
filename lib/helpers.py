from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name_ = input("Enter employee name: ")
    employee = Employee.find_by_name(name_)
    print(employee) if employee else print(
        f"Employee: {name_} not found")


def find_employee_by_id():
    id_ = input("Enter employee id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(
        f'Employee with id: {_id} not found'
    )


def create_employee():
    name = input("Enter employee name: ")
    job_title = input("Enter job title: ")
    department = input("Enter department id: ")
    if Department.find_by_id(department):
        try:
            create = Employee.create(name, job_title, int(department))
            print(f"Success: Employee {create} created ")
        except Exception as e:
            print("Create employee error:", e)
    else:
        print(f'Department {department} not found')
    


def update_employee():
    id_ = input("Enter the Employees's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employees's new name: ")
            department.name = name
            job_title = input("Enter the employees's new job title: ")
            department.job_title = job_title
            department = input("Enter the employees's new department id: ")
            department.department = department

            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {id_} not found')


def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')



def list_department_employees():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        employees = department.employees()
        for employee in employees:
            print(employee)
    else:
        print(f'Department with id: {id_} not found')