import os
from config import STUDENT_FILE
import pandas as pd


def add_Student(new_record): ## ADDING STUDENT IN RECORD

    df = pd.DataFrame([new_record], columns=["Roll No.", "Name", "Marks"])
    df.to_csv(STUDENT_FILE, mode="a", index=False, header=False)
    print("Student record added successfully.")
    return


def record_view(): ## DISPLAY ALL RECORDS
    try:
            df = pd.read_csv(STUDENT_FILE,header=None, names=["Roll No.", "Name", "Marks"])
            if df.empty:
                print("No student records found.")
                return 
            df = df.sort_values("Roll No.")
            print("\n" + df.to_string(index=False))
            return 
    except FileNotFoundError:
        print("File not found.")


def search_student(search_no): ## SEARCH STUDENT IN RECORDS
    try:
            df = pd.read_csv(STUDENT_FILE, header=None, names=["Roll No.", "Name", "Marks"])
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
        df = pd.read_csv(STUDENT_FILE, header=None, names=["Roll No.", "Name", "Marks"])
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
    df = pd.read_csv("student.txt", names=["Roll No","Names","Marks"], dtype={"Roll No": int})
    mask = df["Roll No"] == search_num
    if mask.any():
            return False # Roll No already assigned.
    return True # Not assigned Roll No.
