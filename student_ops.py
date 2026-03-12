import os
from config import STUDENT_FILE
try:
    import pandas as pd
except ImportError:
    pd = None


def add_Student(new_record): ## ADDING STUDENT IN RECORD
    try:
            df = pd.DataFrame([new_record], columns=["Roll No.", "Name", "Marks"])
            if os.path.exists(STUDENT_FILE) and os.path.getsize(STUDENT_FILE) > 0:
                df.to_csv(STUDENT_FILE, mode="a", index=False, header=False)
            else:
                df.to_csv(STUDENT_FILE, mode="a", index=False, header=False)
            print("Student record added successfully.")
            return
    except FileNotFoundError:
        print("File not found.")


def record_view(): ## DISPLAY ALL RECORDS
    try:
            df = pd.read_csv(STUDENT_FILE,header=None, names=["Roll No.", "Name", "Marks"])
            if df.empty:
                print("No student records found.")
                return 
            df = df.sort_values(by = "Roll No.")
            print("\n" + df.to_string(index=False))
            return 
    except FileNotFoundError:
        print("File not found.")


def search_student(search_no): ## SEARCH STUDENT IN RECORDS
    try:
            df = pd.read_csv(STUDENT_FILE, header=None, names=["Roll No.", "Name", "Marks"])
            df["Roll No."] = df["Roll No."].astype(str).str.strip()
            search_no = str(search_no).strip()
            match = df[df["Roll No."] == search_no]
            if not match.empty:
                column = match.iloc[0]
                print("Name:", column["Name"])
                print("Marks:", column["Marks"])
                return
            print("Student record not found.")
            return
    except FileNotFoundError:
        print("File not found.")


def update_marks(search_no, new_marks):  ## UPDATE MARKS IN RECORDS
    try:
        if pd is not None:
            df = pd.read_csv(STUDENT_FILE, header=None, names=["Roll No.", "Name", "Marks"])
            df["Roll No."] = df["Roll No."].astype(str).str.strip()
            new_marks = int(new_marks)
            # Keep marks as int for consistency if stored as numeric
            df.loc[mask := (df["Roll No."] == search_no), "Marks"] = new_marks
            if mask.any():
                df.to_csv(STUDENT_FILE, index=False, header=False)
                print("Record is updated.")
            else:
                print("Record not found.")
            return
    except FileNotFoundError:
        print("File not found.")


def delete_student(search_no): ## DELETING STUDENT RECORD
    try:
            df = pd.read_csv(STUDENT_FILE, header=None, names=["Roll No.", "Name", "Marks"])
            df["Roll No."] = df["Roll No."].astype(str).str.strip()
            search_no = str(search_no).strip()
            mask = df["Roll No."] == search_no
            if mask.any():
                df = df.loc[~mask]
                df.to_csv(STUDENT_FILE, index=False, header=False)
                print("Student record is deleted.")
            else:
                print("Record not found.")
            return
    except FileNotFoundError:
        print("File not found.")


def is_unique(search_num): ## FINDING WHETHER ROLL NO IS UNIQUE OR NOT
    search_num = str(search_num).strip()
    with open(STUDENT_FILE, "r") as file:
        for line in file:
            row = line.strip().split(",")
            if row and row[0].strip() == search_num:
                return False
        return True
