import csv
import os

def add_Student(new_record):
    try:
        with open("student.txt","a",newline="") as file:
         csv.writer(file).writerow(new_record)
         print("Student record added successfully.")
    except FileNotFoundError:
        print("File not found.")

def record_view():
    try:
        with open("student.txt","r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

        
def search_student(search_no):
    try:
        with open("student.txt","r") as file:
            for line in file:
                record_list = line.strip().split(",")
                if record_list[0] == str(search_no):
                    print("Name: ",record_list[1])
                    print("Marks: ",record_list[2])
                    return
            print("Student record not found.") 
            return   
    except FileNotFoundError:
        print("File not found.")


def update_marks(search_no,new_marks):
    try:

    except FileNotFoundError:
        print("File not found.")
