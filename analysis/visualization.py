# analysis/visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Subjects list
subjects = ["Maths", "Science", "English"]


# ==============================
# BAR GRAPH - Average Marks
# ==============================
def bar_avg_marks(df):
    avg_marks = df[subjects].mean()

    plt.figure(figsize=(6, 4))
    bars = plt.bar(subjects, avg_marks)

    # Add labels on bars
    for bar in bars:
        y = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, y, round(y, 2), ha="center")

    plt.title("Average Marks of Class 10 Students")
    plt.ylabel("Marks")
    plt.savefig("graphs/bar_avg_marks.png")
    plt.close()


# ==============================
# LINE GRAPH - Student Percentage Trend
# ==============================
def line_percentage(df):
    df["Percentage"] = df[subjects].mean(axis=1)

    plt.figure(figsize=(8, 4))
    plt.plot(df["ID"], df["Percentage"], marker="o")
    plt.title("Student Percentage Trend")
    plt.xlabel("Student ID")
    plt.ylabel("Percentage")
    plt.savefig("graphs/line_percentage.png")
    plt.close()


# ==============================
# HISTOGRAM - Maths Marks Distribution
# ==============================
def histogram_marks(df):
    plt.figure(figsize=(6, 4))
    plt.hist(df["Maths"], bins=10)
    plt.title("Maths Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.savefig("graphs/hist_maths.png")
    plt.close()


# ==============================
# SCATTER PLOT - Age vs Percentage
# ==============================
def scatter_age_percentage(df):
    df["Percentage"] = df[subjects].mean(axis=1)

    plt.figure(figsize=(6, 4))
    plt.scatter(df["Age"], df["Percentage"])
    plt.title("Age vs Percentage")
    plt.xlabel("Age")
    plt.ylabel("Percentage")
    plt.savefig("graphs/scatter_age_percentage.png")
    plt.close()


# ==============================
# HEATMAP - Correlation
# ==============================
def heatmap_correlation(df):
    plt.figure(figsize=(6, 4))
    corr = df[subjects + ["Age"]].corr()
    sns.heatmap(corr, annot=True)
    plt.title("Correlation Heatmap")
    plt.savefig("graphs/heatmap_corr.png")
    plt.close()


# ==============================
# BOX PLOT - Outliers
# ==============================
def box_plot_marks(df):
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df[subjects])
    plt.title("Box Plot for Marks")
    plt.savefig("graphs/box_marks.png")
    plt.close()


# ==============================
# VIOLIN PLOT - Distribution Shape
# ==============================
def violin_plot_marks(df):
    plt.figure(figsize=(6, 4))
    sns.violinplot(data=df[subjects])
    plt.title("Violin Plot for Marks")
    plt.savefig("graphs/violin_marks.png")
    plt.close()


# ==============================
# MAIN VISUALIZE FUNCTION
# ==============================
def visualize():
    try:
        print("📊 Loading cleaned dataset...")

        # Create graphs folder
        os.makedirs("graphs", exist_ok=True)

        # Load cleaned data
        df = pd.read_csv("cleaned_data/clean_students.csv")

        # Run all graphs
        bar_avg_marks(df)
        line_percentage(df)
        histogram_marks(df)
        scatter_age_percentage(df)
        heatmap_correlation(df)
        box_plot_marks(df)
        violin_plot_marks(df)

        print("✅ All graphs saved in graphs/ folder")

    except Exception as e:
        print("❌ Visualization Error:", e)


# Run directly (optional)
if __name__ == "__main__":
    visualize()
