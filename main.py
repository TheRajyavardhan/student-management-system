import student_ops as so


class Student:
    def __init__(self, roll_no, st_name, st_marks):
        self.roll_num = roll_no
        self.name = st_name
        self.marks = st_marks


def main():
    is_stop = False

    while is_stop != True:

        print("\n---Student Management System---")
        print("1. Add student")
        print("2. View all student")
        print("3. Search student by roll number")
        print("4. Update student marks")
        print("5. Delete student")
        print("6. Exit")
        selected_option = int(input("Enter your ans: "))

        if selected_option == 1:
            stop_adding = False
            while stop_adding != True:
                roll_num = int(input("Enter student roll number: "))
                name = input("Enter student name: ")
                marks = int(input("Enter student marks: "))
                so.add_Student([roll_num, name, marks])
                ans = input("do you want to add more student record? y/n.")
                if ans == "n":
                    stop_adding = True

        elif selected_option == 2:
            so.record_view()

        elif selected_option == 3:
            search_num = input("Enter roll number: ")
            so.search_student(search_num)

        elif selected_option == 4:
            search_num = input("Enter roll number: ")
            new_marks = input("Enter new marks: ")
            so.update_marks(search_num, new_marks)

        elif selected_option == 5:
            search_num = input("Enter roll number: ")
            so.delete_student(search_num)

        elif selected_option == 6:
            ans = input("Do you want to stop the existing program? (y/n).").lower()
            if ans == "y":
                input("Existing program is terminated.")
                is_stop = True

                continue
        elif selected_option > 6 or selected_option < 1:
            print("Input is invalid. Try again.")


if __name__ == "__main__":
    mai