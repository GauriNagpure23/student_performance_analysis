import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create graphs folder
os.makedirs("graphs", exist_ok=True)

# Load cleaned data
df = pd.read_csv("processed_data/cleaned_students.csv")

subjects = ["Maths", "Science", "English"]


# ==============================
# 1️⃣ BAR GRAPH - Average Marks
# ==============================
def bar_avg_marks():
    avg_marks = df[subjects].mean()

    plt.figure(figsize=(6,4))
    bars = plt.bar(subjects, avg_marks)

    # Add labels
    for bar in bars:
        y = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, y, round(y,2), ha='center')

    plt.title("Average Marks of Class 10 Students")
    plt.ylabel("Marks")
    plt.savefig("graphs/bar_avg_marks.png")
    plt.close()


# ==============================
# 2️⃣ LINE GRAPH - Student Percentage Trend
# ==============================
def line_percentage():
    df["Percentage"] = df[subjects].mean(axis=1)

    plt.figure(figsize=(8,4))
    plt.plot(df["ID"], df["Percentage"], marker='o')
    plt.title("Student Percentage Trend")
    plt.xlabel("Student ID")
    plt.ylabel("Percentage")
    plt.savefig("graphs/line_percentage.png")
    plt.close()


# ==============================
# 3️⃣ HISTOGRAM - Marks Distribution
# ==============================
def histogram_marks():
    plt.figure(figsize=(6,4))
    plt.hist(df["Maths"], bins=10)
    plt.title("Maths Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.savefig("graphs/hist_maths.png")
    plt.close()


# ==============================
# 4️⃣ SCATTER PLOT - Age vs Percentage
# ==============================
def scatter_age_percentage():
    df["Percentage"] = df[subjects].mean(axis=1)

    plt.figure(figsize=(6,4))
    plt.scatter(df["Age"], df["Percentage"])
    plt.title("Age vs Percentage")
    plt.xlabel("Age")
    plt.ylabel("Percentage")
    plt.savefig("graphs/scatter_age_percentage.png")
    plt.close()


# ==============================
# 5️⃣ HEATMAP - Correlation
# ==============================
def heatmap_correlation():
    plt.figure(figsize=(6,4))
    corr = df[subjects + ["Age"]].corr()
    sns.heatmap(corr, annot=True)
    plt.title("Correlation Heatmap")
    plt.savefig("graphs/heatmap_corr.png")
    plt.close()


# ==============================
# 6️⃣ BOX PLOT - Outliers Detection
# ==============================
def box_plot_marks():
    plt.figure(figsize=(6,4))
    sns.boxplot(data=df[subjects])
    plt.title("Box Plot for Marks")
    plt.savefig("graphs/box_marks.png")
    plt.close()


# ==============================
# 7️⃣ VIOLIN PLOT - Marks Distribution Shape
# ==============================
def violin_plot_marks():
    plt.figure(figsize=(6,4))
    sns.violinplot(data=df[subjects])
    plt.title("Violin Plot for Marks")
    plt.savefig("graphs/violin_marks.png")
    plt.close()


# ==============================
# RUN ALL GRAPHS
# ==============================
def generate_all_graphs():
    bar_avg_marks()
    line_percentage()
    histogram_marks()
    scatter_age_percentage()
    heatmap_correlation()
    box_plot_marks()
    violin_plot_marks()
    print("All graphs saved in graphs/ folder")


if __name__ == "__main__":
    generate_all_graphs()
