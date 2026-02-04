import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.logger import get_logger

logger = get_logger()

def visualize():
    try:
        df = pd.read_csv("cleaned_data/clean_students.csv")

        # Calculate Total & Percentage
        df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
        df["Percentage"] = df["Total"] / 3

        # -------------------------------
        # 1️⃣ Average Marks per Subject
        subject_avg = df[["Maths","Science","English"]].mean()
        plt.figure()
        subject_avg.plot(kind="bar", title="Average Marks per Subject")
        plt.ylabel("Marks")
        plt.savefig("graphs/subject_average.png")
        plt.close()

        # -------------------------------
        # 2️⃣ Student Percentage Comparison
        plt.figure(figsize=(10,5))
        plt.bar(df["Name"], df["Percentage"])
        plt.title("Student Percentage Comparison")
        plt.xlabel("Student Name")
        plt.ylabel("Percentage")
        plt.xticks(rotation=45)
        plt.savefig("graphs/student_percentage.png")
        plt.close()

        # -------------------------------
        # 3️⃣ Percentage Histogram
        plt.figure()
        plt.hist(df["Percentage"], bins=10)
        plt.title("Percentage Distribution")
        plt.xlabel("Percentage")
        plt.ylabel("Count")
        plt.savefig("graphs/percentage_histogram.png")
        plt.close()

        # -------------------------------
        # 4️⃣ Correlation Heatmap
        plt.figure(figsize=(8,6))
        sns.heatmap(df[["Maths","Science","English","Age"]].corr(), annot=True)
        plt.title("Correlation Heatmap")
        plt.savefig("graphs/correlation_heatmap.png")
        plt.close()

        # -------------------------------
        # 5️⃣ Box Plot (Outliers)
        plt.figure()
        sns.boxplot(data=df[["Maths","Science","English"]])
        plt.title("Marks Outliers Boxplot")
        plt.savefig("graphs/marks_boxplot.png")
        plt.close()

        # -------------------------------
        # Print Toppers
        for sub in ["Maths", "Science", "English"]:
            topper = df.loc[df[sub].idxmax()]
            print(f"Topper in {sub}: {topper['Name']} - {topper[sub]}")

        logger.info("Graphs generated and saved successfully")
        return "Graphs saved in graphs/ folder"

    except Exception as e:
        logger.error(f"Visualization error: {e}")
        return str(e)
