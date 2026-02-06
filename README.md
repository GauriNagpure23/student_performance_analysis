# 📘 Student Data Analysis & Cleaning Project

## 📌 Project Title

**Student Data Analysis and Preprocessing Pipeline using Python**

------------------------------------------------------------------------

## 📖 Project Description

This project focuses on **cleaning, preprocessing, and analyzing messy
student academic data**.\
Real-world datasets often contain missing values, incorrect entries, and
duplicates. This project simulates such scenarios and builds a **robust
data cleaning pipeline**.

The cleaned data can later be used for **data visualization and machine
learning models**.

------------------------------------------------------------------------

## 🚀 Features Implemented

### ✅ Data Cleaning

-   Remove invalid records\
-   Fix duplicate Student IDs\
-   Convert incorrect data types

### ✅ Missing Value Handling

-   Fill missing names with `"Unknown"`\
-   Fill missing marks with student's average\
-   Ask user to manually enter marks if all marks are missing

### ✅ Data Validation

-   Class must be **10** (manual correction if wrong)\
-   Age must be **≥ 15** (manual correction if wrong)

### ✅ Logging System

-   Logs preprocessing steps and errors

### ✅ Visualization

-   Bar Graph\
-   Line Graph\
-   Histogram\
-   Scatter Plot\
-   Heatmap\
-   Box Plot\
-   Violin Plot

------------------------------------------------------------------------

## 📂 Project Structure

    student_data_analysis_project/
    │
    ├── raw_data/
    │   └── dirty_students.csv
    │
    ├── cleaned_data/
    │   └── clean_students.csv
    │
    ├── analysis/
    │   ├── preprocessing.py
    │   └── visualization.py
    │
    ├── utils/
    │   └── logger.py
    │
    ├── main.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python\
-   Pandas\
-   Matplotlib\
-   Seaborn\
-   Logging Module\
-   Git & GitHub

------------------------------------------------------------------------

## ⚙️ How to Run the Project

### Step 1: Clone Repository

``` bash
git clone https://github.com/your-username/student_data_analysis_project.git
cd student_data_analysis_project
```

### Step 2: Install Libraries

``` bash
pip install -r requirements.txt
```

### Step 3: Run

``` bash
python main.py
```

------------------------------------------------------------------------

## 📊 Output

-   Cleaned dataset → `cleaned_data/clean_students.csv`
-   Graphs → `graphs/` folder

------------------------------------------------------------------------

## 🧠 Learning Outcomes

-   Real-world data preprocessing\
-   Pandas data cleaning\
-   Human-in-the-loop validation\
-   Data visualization\
-   Git workflow\
-   Documentation

------------------------------------------------------------------------

## 👩‍💻 Author

**Gauri Nagpure**\
AI/ML Intern \| Python Developer

------------------------------------------------------------------------

## 🔧 Git Commands

``` bash
git init
git status
git add .
git commit -m "Initial commit"
git branch feature-preprocessing
git checkout feature-preprocessing
git remote add origin <repo_url>
git push -u origin feature-preprocessing
git checkout main
git merge feature-preprocessing
git push origin main
```
