
from pydantic import BaseModel
from typing import Optional
from datetime import date

class TableSelection(BaseModel):
    table_name: str


class EmployeeClass(BaseModel):
    id :int
    name:str
    age:int
    department:str
    hire_date:date


class DepartmentClass(BaseModel):
    id:int
    name:str

class DeleteRequest(BaseModel):
    table_name: str
    record_id: int