import pandas as pd
from utils.logger import get_logger

logger = get_logger()

SUBJECTS = ["Maths", "Science", "English"]

# ---------------------------
# Fill missing marks row-wise
# ---------------------------
def fill_marks_row_wise(row):
    values = row[SUBJECTS]
    avg = values.dropna().mean()

    # If some marks missing → fill with student avg
    if not pd.isna(avg):
        for sub in SUBJECTS:
            if pd.isna(row[sub]):
                row[sub] = avg

    return row


# ---------------------------
# Ask user to fix errors
# ---------------------------
def manual_fix(row):
    student_id = row["ID"]
    name = row["Name"]

    print(f"\n⚠️ Checking Student ID {student_id} | Name: {name}")

    # ---- CLASS CHECK ----
    if row["Class"] != 10:
        print(f"❌ Invalid Class found: {row['Class']} (Expected 10)")
        new_class = input("Enter correct class (should be 10): ")
        row["Class"] = int(new_class)

    # ---- AGE CHECK ----
    if pd.isna(row["Age"]) or row["Age"] < 15:
        print(f"❌ Invalid Age found: {row['Age']}")
        new_age = input("Enter correct age (>=15): ")
        row["Age"] = int(new_age)

    # ---- MARKS CHECK ----
    if row[SUBJECTS].isna().all():
        print("❌ All marks missing!")
        for sub in SUBJECTS:
            mark = input(f"Enter {sub} marks: ")
            row[sub] = float(mark)

    return row


# ---------------------------
# Main Cleaning Function
# ---------------------------
def clean_data():
    try:
        df = pd.read_csv("raw_data/dirty_students.csv")

        # Convert to numeric
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
        df["Class"] = pd.to_numeric(df["Class"], errors="coerce")

        for sub in SUBJECTS:
            df[sub] = pd.to_numeric(df[sub], errors="coerce")

        # Keep only rows with ID
        df = df[df["ID"].notnull()]

        # Fix duplicate IDs
        dup_ids = df[df.duplicated("ID", keep="first")]
        for idx in dup_ids.index:
            df.at[idx, "ID"] = df["ID"].max() + 1

        # Fill missing names
        df["Name"].fillna("Unknown", inplace=True)

        # ---------------- MANUAL ERROR CHECK ----------------
        # Only rows with errors will be asked
        error_mask = (
            (df["Class"] != 10) |
            (df["Age"].isna()) |
            (df["Age"] < 15) |
            (df[SUBJECTS].isna().all(axis=1))
        )

        df.loc[error_mask] = df[error_mask].apply(manual_fix, axis=1)

        # ---------------- AUTO MARK FILL ----------------
        df = df.apply(fill_marks_row_wise, axis=1)

        # Save cleaned file
        df.to_csv("cleaned_data/clean_students.csv", index=False)
        logger.info("Preprocessing completed successfully")

        print("\n✅ Data Cleaning Completed Successfully")
        return df

    except Exception as e:
        logger.error(e)
        print("❌ Error:", e)
        return None


# Run
if __name__ == "__main__":
    clean_data()
