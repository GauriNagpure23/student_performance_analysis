import pandas as pd
from utils.logger import get_logger

logger = get_logger()

def fill_marks_row_wise(row):
    subjects = ["Maths", "Science", "English"]
    values = row[subjects]

    # Calculate student average from available marks
    avg = values.dropna().mean()

    for sub in subjects:
        if pd.isna(row[sub]):
            row[sub] = avg  # fill with student's own avg

    return row


def clean_data():
    try:
        df = pd.read_csv("raw_data/dirty_students.csv")

        # Convert to numeric
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
        for sub in ["Maths","Science","English"]:
            df[sub] = pd.to_numeric(df[sub], errors="coerce")

        # Keep rows if ID exists
        df = df[df["ID"].notnull()]

        # Fix duplicate IDs
        dup_ids = df[df.duplicated("ID", keep="first")]
        for idx in dup_ids.index:
            df.at[idx, "ID"] = df["ID"].max() + 1

        # Fill missing names
        df["Name"].fillna("Unknown", inplace=True)

        # Fill missing age with class allowed avg age (15)
        df["Age"].fillna(15, inplace=True)

        # Fill marks using student's own average
        df = df.apply(fill_marks_row_wise, axis=1)

        # Save cleaned data
        df.to_csv("processed_data/cleaned_students.csv", index=False)
        logger.info("Preprocessing completed successfully")

        return df

    except Exception as e:
        logger.error(e)
        return None
