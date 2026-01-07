from pydanticFile import Student
data_ok = {
    "name": "Ravi",
    "age": 20,
    "subjects": ["Math", "Science"]
}

student_ok = Student(**data_ok)
print(student_ok)
print(student_ok.model_dump())
