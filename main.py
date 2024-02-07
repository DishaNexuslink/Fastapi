from fastapi import FastAPI, Request,HTTPException,Form,File,UploadFile
from enum import Enum

from schemaFile  import schema
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



@app.post("/form/data")
def form_data(data:schema):
    return {"username":data.username,"Mobile_Number":data.Mobile_Number}

# -------------file upload------
@app.post("/file/bytes")
def file_data(file:bytes=File()):
    return {"file":len(file)}

@app.post("/file")
async def file_info(file1: UploadFile = UploadFile(...),file2: UploadFile = UploadFile(...)):
    # contents = await file.read()
    
    # # Try decoding with different encodings
    # encodings_to_try = ["utf-8", "latin-1", "iso-8859-1", "windows-1252"]  
    # decoded_contents = None
    # for encoding in encodings_to_try:
    #     try:
    #         decoded_contents = contents.decode(encoding)
    #         break
    #     except UnicodeDecodeError:
    #         continue
    
    # if decoded_contents is None:
    #     return {"error": "Unable to decode file contents with any encoding"}
    
    return {"filename1": file1.filename,"filename2": file2.filename}


