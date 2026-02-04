import pandas as pd
from utils.validators import *
from utils.logger import get_logger

logger = get_logger()

FILE_PATH = "raw_data/dirty_students.csv"


def read_csv():
    # simple function to read file
    try:
        data = pd.read_csv(FILE_PATH)
        return data
    except Exception as err:
        logger.error("Error reading file: " + str(err))
        return None


def append_student(name, age, cls, maths, science, english):
    try:
        # checking name
        result = validate_name(name)
        if result != True:
            return result

        # checking age
        result = validate_age(age)
        if result != True:
            return result

        # checking marks
        marks = [maths, science, english]
        for m in marks:
            result = validate_marks(m)
            if result != True:
                return result

        df = pd.read_csv(FILE_PATH)

        # create dictionary for new row
        row = {
            "Name": name,
            "Age": age,
            "Class": cls,
            "Maths": maths,
            "Science": science,
            "English": english
        }

        df.loc[len(df)] = row
        df.to_csv(FILE_PATH, index=False)

        logger.info("Added new student")
        return "Student added"

    except Exception as err:
        logger.error("Error adding student: " + str(err))
        return "Something went wrong"


def delete_student(name):
    try:
        df = pd.read_csv(FILE_PATH)

        # remove student
        df = df[df["Name"] != name]

        df.to_csv(FILE_PATH, index=False)
        logger.info("Deleted student " + name)

        return "Student removed"

    except Exception as err:
        logger.error("Error deleting student: " + str(err))
        return "Delete failed"
    