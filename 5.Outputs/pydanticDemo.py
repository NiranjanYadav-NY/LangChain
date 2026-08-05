from pydantic import BaseModel, EmailStr,  Field
from typing import TypedDict, Annotated, Optional 

class Student(BaseModel):
    name:  str = 'Niranjan'
    age: Optional[int] = None
    email: EmailStr
    cgpa : float = Field(gt = 0, lt=10, default=5, description='A decimal value representing the cgpa of the student')

new_student = {'name': 'niranjan', 'email':' '} 
student = Student(**new_student)
student_dict = dict(student)
print(student)

student_json = student.model_dump_json()
#pydantic tries to udnerstand the data from itself!
