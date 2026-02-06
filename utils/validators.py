from utils.custom_exceptions import *

def validate_class(cls):
    if str(cls) != "10":
        return "Only Class 10 students allowed"
    return True

def validate_age(age):
    try:
        age = int(age)
        if age < 15 or age > 16:
            return "Age must be between 14 and 16"
        return True
    except:
        return "Invalid age"

def validate_marks(m):
    try:
        m = float(m)
        if m < 0 or m > 100:
            return "Marks must be 0-100"
        return True
    except:
        return "Invalid marks"
def validate_name(name):
    if name.isalpha():
        return True
    else:
        return "Invalid Name"
