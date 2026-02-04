from utils.custom_exceptions import *

def validate_name(name):
    try:
        if not name.isalpha():
            raise InvalidNameError("Name must contain only alphabets")
        return True
    except Exception as e:
        return str(e)

def validate_age(age):
    try:
        age = int(age)
        if age < 3 or age > 100:
            raise InvalidAgeError("Invalid age range")
        return True
    except Exception as e:
        return str(e)

def validate_marks(mark):
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            raise InvalidMarksError("Marks must be 0-100")
        return True
    except Exception as e:
        return str(e)
