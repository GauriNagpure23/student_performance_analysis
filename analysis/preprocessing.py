import pandas as pd
import numpy as np
from utils.logger import get_logger

logger = get_logger()

def clean_data():
    try:
        df = pd.read_csv("raw_data/dirty_students.csv")

        # Remove completely empty rows
        df.dropna(how="all", inplace=True)

        # Clean Name column
        df["Name"] = df["Name"].astype(str).str.strip().str.title()
        df["Name"].replace(["None", "Nan", ""], np.nan, inplace=True)
        df["Name"].fillna("Unknown", inplace=True)

        # Convert Age
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
        df.loc[(df["Age"] < 5) | (df["Age"] > 30), "Age"] = np.nan
        df["Age"].fillna(df["Age"].mean(), inplace=True)

        # Subjects
        subjects = ["Maths", "Science", "English"]
        for sub in subjects:
            df[sub] = pd.to_numeric(df[sub], errors="coerce")
            df.loc[(df[sub] < 0) | (df[sub] > 100), sub] = np.nan
            df[sub].fillna(df[sub].mean(), inplace=True)

        # Remove duplicates
        df.drop_duplicates(inplace=True)

        # Save cleaned file
        df.to_csv("cleaned_data/clean_students.csv", index=False)
        logger.info("Data cleaned successfully")

        return df

    except Exception as e:
        logger.error(e)
        return None
