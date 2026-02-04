import pandas as pd
from utils.validators import *
from utils.logger import get_logger

logger = get_logger()

FILE_PATH = "raw_data/dirty_students.csv"

def read_csv():
    try:
        return pd.read_csv(FILE_PATH)
    except Exception as e:
        logger.error(e)
        return None

def append_student(name, age, cls, m, s, e):
    try:
        if validate_name(name) != True: return validate_name(name)
        if validate_age(age) != True: return validate_age(age)
        for mark in [m, s, e]:
            if validate_marks(mark) != True: return validate_marks(mark)

        df = pd.read_csv(FILE_PATH)
        new_row = {"Name": name, "Age": age, "Class": cls, "Maths": m, "Science": s, "English": e}
        df.loc[len(df)] = new_row
        df.to_csv(FILE_PATH, index=False)
        logger.info("Student added")
        return "Student added successfully"
    except Exception as e:
        logger.error(e)
        return str(e)

def delete_student(name):
    try:
        df = pd.read_csv(FILE_PATH)
        df = df[df["Name"] != name]
        df.to_csv(FILE_PATH, index=False)
        logger.info("Student deleted")
        return "Deleted"
    except Exception as e:
        logger.error(e)
        return str(e)
