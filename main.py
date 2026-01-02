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

        if selected_option == 1:  ## Delete student record
            stop_adding = False
            while stop_adding != True:
                roll_num = input("Enter roll number: ")
                if roll_num.isdigit() == False or int(roll_num) < 1:
                    print("Invalid roll number.")
                    break
                if so.is_unique(roll_num) == False:
                    print("Roll number is already assigned.")
                    break
                name = input("Enter student name: ")
                if name.isalpha() == False:
                    print("Invalid name.")
                    break
                marks = input("Enter marks: ")
                if marks.isdigit() == False or 0 < marks > 100:
                    print("Invalid marks.")
                    break
                so.add_Student([roll_num, name, marks])
                ans = input(
                    "do you want to add more student record? (Enter = yes, n = no).."
                ).lower()
                if ans == "n":
                    stop_adding = True

        elif selected_option == 2:  ## View all records
            so.record_view()

        elif selected_option == 3:  ## Search student record
            search_num = input("Enter roll number: ")
            if search_num.isdigit() == False or int(search_num) < 1:
                print("Invalid roll number.")
                break
            so.search_student(search_num)

        elif selected_option == 4:  ## Update student record
            stop_update = False
            while stop_update != True:
                search_num = input("Enter roll number: ")
                if search_num.isdigit() == False or int(search_num) < 1:
                    print("Invalid roll number.")
                    break
                new_marks = input("Enter new marks: ")
                if new_marks.isdigit() == False or 0 > int(new_marks) > 100:
                    print("Invalid marks.")
                    break
                so.update_marks(search_num, new_marks)
                ans = input(
                    "Do you want to update another student record? (Enter = yes, n = no).. "
                ).lower()
                if ans == "n":
                    stop_update = True

        elif selected_option == 5:  ## Delete student record
            stop_deleting = False
            while stop_deleting != True:
                search_num = input("Enter roll number: ")
                if search_num.isdigit() == False or int(search_num) < 1:
                    print("Invalid roll number.")
                    break
                so.delete_student(search_num)
                ans = input(
                    "Do you want to delete another student record? (Enter = yes, n = no).. "
                ).lower()
                if ans == "n":
                    stop_deleting = True

        elif selected_option == 6:  ## Exit option
            ans = input("Do you want to stop the existing program? (y/n)... ").lower()
            if ans == "y":
                input("Existing program is terminated.")
                is_stop = True

                continue
        elif selected_option > 6 or selected_option < 1:  ## Invalid input
            print("Input is invalid. Try again.")


if __name__ == "__main__":
    main()