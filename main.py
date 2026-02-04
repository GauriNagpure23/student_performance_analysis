from utils.csv_operations import *
from analysis.preprocessing import clean_data
from analysis.visualization import visualize

def menu():
    while True:
        print("\n1 Add Student")
        print("2 Delete Student")
        print("3 Read CSV")
        print("4 Clean Data")
        print("5 Visualize")
        print("6 Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            print(append_student(
                input("Name: "),
                input("Age: "),
                input("Class: "),
                input("Maths: "),
                input("Science: "),
                input("English: ")
            ))

        elif ch == "2":
            print(delete_student(input("Enter name to delete: ")))

        elif ch == "3":
            print(read_csv())

        elif ch == "4":
            clean_data()
            print("Data cleaned and saved")

        elif ch == "5":
            visualize()

        elif ch == "6":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
