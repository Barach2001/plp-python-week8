"""
Personal Mini-Toolkit
A beginner-friendly menu program with three useful tools.
"""


def study_task_list():
    """Allow the user to add and view study tasks."""
    tasks = []

    while True:
        print("\n--- Study Task List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter your study task: ").strip()
            if task:
                tasks.append(task)
                print("Task added successfully!")
            else:
                print("A task cannot be empty.")
        elif choice == "2":
            if not tasks:
                print("Your task list is empty.")
            else:
                print("\nYour study tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def grade_average_calculator():
    """Collect scores and calculate their average."""
    print("\n--- Grade Average Calculator ---")

    while True:
        try:
            count = int(input("How many scores do you want to enter? "))
            if count > 0:
                break
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number.")

    total = 0

    for number in range(1, count + 1):
        while True:
            try:
                score = float(input(f"Enter score {number} (0-100): "))
                if 0 <= score <= 100:
                    total += score
                    break
                print("Score must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    average = total / count
    print(f"Your average is: {average:.2f}%")

    if average >= 70:
        print("Result: Excellent work!")
    elif average >= 50:
        print("Result: Good effort. Keep practising!")
    else:
        print("Result: Keep studying and try again!")


def basic_calculator():
    """Perform one basic arithmetic calculation."""
    print("\n--- Basic Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter your choice (1-4): ").strip()

    if operation == "1":
        answer = first_number + second_number
    elif operation == "2":
        answer = first_number - second_number
    elif operation == "3":
        answer = first_number * second_number
    elif operation == "4":
        if second_number == 0:
            print("You cannot divide by zero.")
            return
        answer = first_number / second_number
    else:
        print("Invalid operation choice.")
        return

    print(f"Result: {answer:g}")


def main():
    """Show the main menu until the user chooses to quit."""
    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Study Task List")
        print("2. Grade Average Calculator")
        print("3. Basic Calculator")
        print("4. Quit")

        choice = input("Choose a tool (1-4): ").strip()

        if choice == "1":
            study_task_list()
        elif choice == "2":
            grade_average_calculator()
        elif choice == "3":
            basic_calculator()
        elif choice == "4":
            print("Thank you for using the Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
