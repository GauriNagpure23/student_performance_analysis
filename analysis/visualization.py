import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Subjects list
subjects = ["Maths", "Science", "English"]


# ---------------- BAR GRAPH ----------------
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


# ---------------- LINE GRAPH ----------------
def line_percentage(df):
    df["Percentage"] = df[subjects].mean(axis=1)

    plt.figure(figsize=(8, 4))
    plt.plot(df["ID"], df["Percentage"], marker="o")

    plt.title("Student Percentage Trend")
    plt.xlabel("Student ID")
    plt.ylabel("Percentage")
    plt.savefig("graphs/line_percentage.png")
    plt.close()


# ---------------- HISTOGRAM ----------------
def histogram_marks(df):
    plt.figure(figsize=(6, 4))

    counts, bins, patches = plt.hist(df["Maths"], bins=10)

    # Calculate bin centers
    bin_centers = 0.5 * (bins[:-1] + bins[1:])

    # Add labels in the center of bars
    for count, x in zip(counts, bin_centers):
        plt.text(x, count, int(count), ha="center", va="bottom", fontsize=8)

    plt.title("Maths Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.savefig("graphs/hist_maths.png")
    plt.close()



# ---------------- PIE PLOT ----------------
def pie_subject_distribution(df):
    # Calculate average marks per subject
    avg_marks = df[subjects].mean()

    plt.figure(figsize=(6, 6))

    # Create pie chart
    plt.pie(
        avg_marks,
        labels=subjects,
        autopct="%1.1f%%",   # Show percentage on slices
        startangle=90,
    )

    plt.title("Distribution of Marks in Subjects (Maths, Science, English)")
    plt.savefig("graphs/pie_subject_distribution.png")
    plt.close()



# ---------------- HEATMAP ----------------
def heatmap_correlation(df):
    plt.figure(figsize=(6, 4))
    corr = df[subjects + ["Age"]].corr()
    sns.heatmap(corr, annot=True)
    plt.title("Correlation Heatmap")
    plt.savefig("graphs/heatmap_corr.png")
    plt.close()


# ---------------- BOX PLOT ----------------
def box_plot_marks(df):
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df[subjects])
    plt.title("Box Plot for Marks")
    plt.ylabel("Marks")
    plt.savefig("graphs/box_marks.png")
    plt.close()


# ---------------- VIOLIN PLOT ----------------
def violin_plot_marks(df):
    plt.figure(figsize=(6, 4))
    sns.violinplot(data=df[subjects])
    plt.title("Violin Plot for Marks")
    plt.ylabel("Marks")
    plt.savefig("graphs/violin_marks.png")
    plt.close()


# ---------------- MAIN FUNCTION ----------------
def visualize():
    try:
        print("Loading cleaned dataset...")

        # Create graphs folder
        os.makedirs("graphs", exist_ok=True)

        # Load cleaned data
        df = pd.read_csv("cleaned_data/clean_students.csv")

        # Run all graphs
        bar_avg_marks(df)
        line_percentage(df)
        histogram_marks(df)
        pie_subject_distribution(df)
        heatmap_correlation(df)
        box_plot_marks(df)
        violin_plot_marks(df)

        print("All graphs saved in graphs/ folder")

    except Exception as e:
        print("Visualization Error:", e)


# Run directly
if __name__ == "__main__":
    visualize()
