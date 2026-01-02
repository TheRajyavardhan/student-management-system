import csv
import os
from config import STUDENT_FILE, TEMP_FILE


def add_Student(new_record):
    try:
        with open(STUDENT_FILE, "a", newline="") as file:
            csv.writer(file).writerow(new_record)
            print("Student record added successfully.")
            return
    except FileNotFoundError:
        print("File not found.")


def record_view():
    try:
        with open(STUDENT_FILE, "r") as file:
            for row in csv.reader(file):
                print("Roll Number: ", row[0])
                print("Name: ", row[1])
                print("Marks: ", row[2], end="\n\n")
        return
    except FileNotFoundError:
        print("File not found.")


def search_student(search_no):
    try:
        with open(STUDENT_FILE, "r") as file:
            for row in csv.reader(file):
                if row[0] == str(search_no):
                    print("Name:", row[1])
                    print("Marks:", row[2])
                    return
            print("Student record not found.")
            return
    except FileNotFoundError:
        print("File not found.")


def update_marks(search_no, new_marks):
    try:
        is_updated = False
        with open(STUDENT_FILE, "r", newline="") as infile:
            with open(TEMP_FILE, "w", newline="") as outfile:

                reader = csv.reader(infile)
                writer = csv.writer(outfile)

                for row in reader:
                    if row and row[0] == search_no:
                        row[2] = new_marks
                        is_updated = True
                    writer.writerow(row)
        if is_updated:
            os.replace(TEMP_FILE, STUDENT_FILE)
            print("Record is updated.")
        else:
            os.remove(TEMP_FILE)
            print("Record not found.")
        return
    except FileNotFoundError:
        print("File not found.")


def delete_student(search_no):
    try:
        is_deleted = False
        with open(STUDENT_FILE, "r", newline="") as infile:
            with open(TEMP_FILE, "w", newline="") as outfile:

                reader = csv.reader(infile)
                writer = csv.writer(outfile)

                for row in reader:
                    if row and row[0] == search_no:
                        is_deleted = True
                        continue
                    writer.writerow(row)
        if is_deleted:
            os.replace(TEMP_FILE, STUDENT_FILE)
            print("Student record is deleted.")
        else:
            os.remove(TEMP_FILE)
            print("Record not found.")
        return
    except FileNotFoundError:
        print("File not found.")


def is_unique(search_num):
    with open(STUDENT_FILE, "r") as file:
        for line in file:
            row = line.strip().split(",")
            if row[0] == search_num:
                return False
        return True
