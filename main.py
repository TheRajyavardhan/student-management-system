import student_ops as so


def main():
    is_stop = False

    while not is_stop:
        print("="*40)
        print("       Student Management System")
        print("="*40)
        print("1. Add student")
        print("2. Show all student")
        print("3. Search student by roll number")
        print("4. Update student marks")
        print("5. Delete student")
        print("6. Show topper")
        print("7. Show class average")
        print("8. Count total student")
        print("9. Exit")
        print("="*40)
        try:
            selected_option = int(input("Enter your ans: "))
        except ValueError:
            print("Invalid input. Enter a number from 1 to 6.")
            continue

        if selected_option == 1:  ## Add student record
            while True:
                roll_num = int(input("Enter roll number: "))
                if roll_num < 1:
                    print("Invalid roll number.")
                    break
                if not so.is_unique(roll_num):
                    print("Roll number is already assigned.")
                    break
                name = input("Enter student name: ").strip()
                if name.isalpha() == False:
                    print("Invalid name.")
                    break
                marks = int(input("Enter marks: "))
                if not (0 <= marks <= 100):
                    print("Invalid marks.")
                    break
                so.add_Student([roll_num, name, marks])
                ans = input(
                    "do you want to add more student record? (Enter = yes, n = no).."
                ).lower()
                if ans == "n":
                    break

        elif selected_option == 2:  ## View all records
            so.record_view()

        elif selected_option == 3:  ## Search student record
            search_num = int(input("Enter roll number: "))
            if search_num < 1:
                print("Invalid roll number.")
                continue
            so.search_student(search_num)

        elif selected_option == 4:  ## Update student record
            while  True:
                search_num = int(input("Enter roll number: "))
                if search_num < 1:
                    print("Invalid roll number.")
                    break
                new_marks = int(input("Enter new marks: "))
                if not (0 <= new_marks <= 100):
                    print("Invalid marks.")
                    break
                so.update_marks(search_num, new_marks)
                ans = input(
                    "Do you want to update another student record? (Enter = yes, n = no).. "
                ).lower()
                if ans == "n":
                    break

        elif selected_option == 5:  ## Delete student record
            while True:
                search_num = int(input("Enter roll number: "))
                if search_num < 1:
                    print("Invalid roll number.")
                    break
                so.delete_student(search_num)
                ans = input(
                    "Do you want to delete another student record? (Enter = yes, n = no).. "
                ).lower()
                if ans == "n":
                    break
        
        elif selected_option == 6: ## Show topper
            so.show_topper()

        elif selected_option == 7: ## Class average
            so.class_avg()

        elif selected_option == 8: ## Total number of students
            so.total_student()
        elif selected_option == 9:  ## Exit option
            ans = input("Do you want to stop the existing program? (y/n)... ").lower()
            if ans == "y":
                print("Program terminated.")
                is_stop = True

                continue
        else:
            print("Input is invalid. Try again.")


if __name__ == "__main__":
    main()