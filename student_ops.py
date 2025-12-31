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
        is_updated = False
        with open("student.txt","r",newline="") as infile:       
         with open("temp.txt","w",newline="") as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                if row and row[0] == search_no:
                    row[2] = new_marks
                    is_updated = True
                writer.writerow(row)
        if is_updated:
                os.replace("temp.txt","student.txt")
                print("Record is updated.")
        else:
                os.remove("temp.txt")
                print("Record not found.")

    except FileNotFoundError:
        print("File not found.")


def delete_student(search_no):
    try:
        is_deleted = False
        with open("student.txt","r",newline="") as infile:       
         with open("temp.txt","w",newline="") as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                if row and row[0] == search_no:
                    is_deleted = True
                    continue
                writer.writerow(row)
        if is_deleted:
                os.replace("temp.txt","student.txt")
                print("Student record is deleted.")
        else:
                os.remove("temp.txt")
                print("Record not found.")

    except FileNotFoundError:
        print("File not found.")
