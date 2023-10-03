import json

from sqlalchemy import Column, Integer, String, Float

from backend.database.main import Database


class Employee(Database.BASE):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    phone_number = Column(String)
    email_address = Column(String)
    salary = Column(Float)

    def __repr__(self):
        return f"<Employee(employee_id={self.employee_id}, full_name={self.full_name}, salary={self.salary})>"

    def as_dict(self):
        return {
            'employee_id': self.employee_id,
            'full_name': self.full_name,
            'phone_number': self.phone_number,
            'email_address': self.email_address,
            'salary': self.salary
        }

    def as_json(self):
        return json.dumps(self.as_dict())

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


def register_models():
    Database.BASE.metadata.create_all(Database().engine)
