from fastapi import FastAPI, Request,HTTPException,Form 
from enum import Enum
from pydantic import BaseModel


app=FastAPI()

# ------greetings-------
@app.get("/greetings")
async def greetings():
    return ("Greetings from myside ")


# ---------------calculator----------(using selection )
class ModelName(str, Enum):
    addition = "+"
    subtraction = "-"
    multiplication = "*"
    division = "/"

@app.get("/models/{operator}")
def get_model(operator: ModelName, x: int, y: int):
    if operator == ModelName.addition:
        return {"result": x + y}
    elif operator == ModelName.subtraction:
        return {"result": x - y}
    elif operator == ModelName.multiplication:
        return {"result": x * y}
    elif operator == ModelName.division:
        return {"result": x / y}



# ----------------calculator(manual)
@app.get("/calculator/{x}/{y}")
def calc(x: int, y: int, operation: str, operator: str):
    if operation.lower() == "addition" and operator == "+":
        return x + y
    if operation.lower() == "substraction" and operator == "-":
        return x - y
    if operation.lower() == "multiplication" and operator == "*":
        return x * y
    if operation.lower() == "division" and operator == "/":
        return x / y
    return "Invalid operation or operator"


# -------------taking inputs and displaying
@app.get("/details/{name}/{number}")
def details(name:str,number:int):
    return {"name":name,"Mobile Number": number}


# -----------defining scema and use of forms in fastAPI

class schema(BaseModel):
    username:str
    Mobile_Number:int

@app.post("/form/data")
def form_data(data:schema):
    return {"username":data.username,"Mobile_Number":data.Mobile_Number}

# -------------
