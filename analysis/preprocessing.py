import pandas as pd
from utils.logger import get_logger

logger = get_logger()


# ================================
# Fill marks using student's own average
# ================================
def fill_marks_row_wise(row):
    subjects = ["Maths", "Science", "English"]
    values = row[subjects]

    # If all marks missing → ask user manually
    if values.isnull().all():
        print(f"\n Student ID {row['ID']} has NO marks!")
        for sub in subjects:
            while True:
                try:
                    val = float(input(f"Enter {sub} marks for {row['Name']}: "))
                    row[sub] = val
                    break
                except:
                    print(" Enter valid numeric marks!")

        return row

    # Otherwise fill missing with student's own average
    avg = values.dropna().mean()

    for sub in subjects:
        if pd.isna(row[sub]):
            row[sub] = avg

    return row


# ================================
# MAIN CLEANING FUNCTION
# ================================
def clean_data():
    try:
        df = pd.read_csv("raw_data/dirty_students.csv")

        # Convert numeric
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
        for sub in ["Maths", "Science", "English"]:
            df[sub] = pd.to_numeric(df[sub], errors="coerce")

        # Keep rows only if ID exists
        df = df[df["ID"].notnull()]

        # Fix duplicate IDs
        dup_ids = df[df.duplicated("ID", keep="first")]
        for idx in dup_ids.index:
            new_id = df["ID"].max() + 1
            print(f" Duplicate ID found! Assigning new ID {new_id}")
            df.at[idx, "ID"] = new_id

        # Fill missing names
        df["Name"].fillna("Unknown", inplace=True)

        # Fill missing age with default class 10 age
        df["Age"].fillna(15, inplace=True)

        # ================= CLASS VALIDATION =================
        for idx, row in df.iterrows():
            if row["Class"] != 10:
                print(f"\n Student ID {row['ID']} has Class = {row['Class']}")
                while True:
                    ans = input("Update class to 10? (y/n): ")
                    if ans.lower() == "y":
                        df.at[idx, "Class"] = 10
                        break
                    elif ans.lower() == "n":
                        print("Skipping student (keeping wrong class).")
                        break
                    else:
                        print("Enter y or n")

        # ================= AGE VALIDATION =================
        for idx, row in df.iterrows():
            if row["Age"] < 15:
                print(f"\n Student ID {row['ID']} has Age = {row['Age']} (Invalid for Class 10)")
                while True:
                    try:
                        new_age = int(input("Enter corrected age (>=15): "))
                        if new_age >= 15:
                            df.at[idx, "Age"] = new_age
                            break
                        else:
                            print(" Age must be 15 or above")
                    except:
                        print(" Enter valid integer age!")

        # ================= MARKS CLEANING =================
        df = df.apply(fill_marks_row_wise, axis=1)

        # Save cleaned file
        df.to_csv("cleaned_data/clean_students.csv", index=False)
        logger.info("Preprocessing completed successfully")

        print("\n Cleaned data saved to cleaned_data/clean_students.csv")
        return df

    except Exception as e:
        logger.error(e)
        print(" Error in preprocessing:", e)
        return None
