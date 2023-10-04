import eel

from backend.database.employees.model import Employee
from backend.database.main import Database

session = Database().session


def as_dict(employees):
    return [employee.as_dict() for employee in employees]


@eel.expose
def create(full_name: str,
           phone_number: str = None,
           email_address: str = None,
           salary: float = None):
    employee = Employee(full_name=full_name,
                        phone_number=phone_number,
                        email_address=email_address,
                        salary=salary)
    session.add(employee)
    session.commit()
    return employee.as_dict()


@eel.expose
def get_by_id(employee_id: int):
    return (session.query(Employee)
            .filter(Employee.employee_id == employee_id).first()
            .as_dict())


@eel.expose
def get(limit: int = None):
    if limit is None:
        return as_dict(session.query(Employee).all())

    return as_dict(session.query(Employee).limit(limit).all())


@eel.expose
def get_like(field: str, value: str):
    field = getattr(Employee, field)
    return as_dict(session.query(Employee).filter(field.like(f'%{value}%')).all())


@eel.expose
def edit(employee_id: int,
         full_name: str = None,
         phone_number: str = None,
         email_address: str = None,
         salary: float = None):
    employee = session.query(Employee).filter(Employee.employee_id == employee_id).first()
    employee.full_name = full_name or employee.full_name
    employee.phone_number = phone_number or employee.phone_number
    employee.email_address = email_address or employee.email_address
    employee.salary = salary or employee.salary
    session.commit()
    return employee.as_dict()


@eel.expose
def delete(employee_id: int):
    employee = session.query(Employee).filter(Employee.employee_id == employee_id).first()
    session.delete(employee)
    session.commit()
    return True


@eel.expose
def delete_many(employee_ids: list):
    for employee_id in employee_ids:
        employee = session.query(Employee).filter(Employee.employee_id == employee_id).first()
        session.delete(employee)
    session.commit()
