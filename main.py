from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from utils import *
from schemas import *
import sys,uvicorn
from exception_logger import CustomException
from query import *
from sqlalchemy.exc import IntegrityError


app = FastAPI()

# --------------show table-------------
@app.get("/showTable")
def list_of_table():
    return show_table(show_table_query)


# -----------------Create------------
@app.post("/create")
def create_record(table: TableSelection, Employee: EmployeeClass, Department: DepartmentClass):
    try:
        if table.table_name.lower() == "employee_table":
            if Employee.id is None:
                raise HTTPException(status_code=400, detail="Employee data not provided")
            
            query = f"""INSERT INTO employee_table (id, name, age, department, hire_date) 
                        VALUES ({Employee.id}, "{Employee.name}", {Employee.age}, "{Employee.department}", "{Employee.hire_date}");"""
            
        elif table.table_name.lower() == "department_table":
            if Department.id is None:
                raise HTTPException(status_code=400, detail="Department data not provided")
            
            query = f"""INSERT INTO department_table (id, name) 
                        VALUES ({Department.id}, "{Department.name}");"""
        else:
            return {"message": f"Invalid table name: {table.table_name}"}

        inserted = execute(query)
     

    except IntegrityError as ie:
        error_detail = "Duplicate value for primary key"
        return HTTPException(status_code=400, detail=error_detail)

    except HTTPException as he:
        raise he 

    except Exception as e:
        print(CustomException(e, sys))
        raise HTTPException(status_code=500, detail="Internal Server Error")

    


@app.post("/read")
def read(table: TableSelection):
    try:
        if table.table_name.lower() not in ["employee_table", "department_table"]:
            raise HTTPException(status_code=400, detail="Invalid table name")

        query = f"SELECT * FROM {table.table_name};"

        # Execute the query to fetch data
        data = read_data(query)

        # Return the fetched data
        return {"data": data}

    except HTTPException as he:
        raise he
    except Exception as e:
        print(CustomException(e, sys))
        raise HTTPException(status_code=500, detail="Internal Server Error")



def delete_record(request: DeleteRequest):
    try:
        if request.table_name.lower() not in ["employees", "departments"]:
            raise HTTPException(status_code=400, detail="Invalid table name")

       
        query = f"DELETE FROM {request.table_name} WHERE id = {request.record_id};"

        deleted = execute(query)

        if deleted:
            return {"message": "Record deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail=f"Record with id {request.record_id} not found")

    except HTTPException as he:
        raise he
    except Exception as e:
        print(CustomException(e, sys))
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8080)






# @app.put("/update")
# def update_record(table: TableSelection, user_id: Optional[int] = None, item_id: Optional[int] = None, user: User = None, item: Item = None):
#     if table.table_name.lower() == "user":
#         if user_id is None or user is None:
#             raise HTTPException(status_code=400, detail="User ID or data not provided")
#         return update_user(user_id, user)
#     elif table.table_name.lower() == "item":
#         if item_id is None or item is None:
#             raise HTTPException(status_code=400, detail="Item ID or data not provided")
#         return update_item(item_id, item)
#     else:
#         raise HTTPException(status_code=400, detail="Invalid table name")