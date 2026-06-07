while True:

    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        task = input("Enter Task: ")

        file = open("tasks.txt", "a")

        file.write(task + "\n")

        file.close()

        print("Task Added Successfully!")

    elif choice == "2":

        file = open("tasks.txt", "r")

        tasks = file.readlines()

        file.close()

        print("\nYour Tasks:")

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

    elif choice == "3":

        file = open("tasks.txt", "r")

        tasks = file.readlines()

        file.close()

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        task_num = int(input("Enter Task Number To Delete: "))

        if 1 <= task_num <= len(tasks):

            tasks.pop(task_num - 1)

            file = open("tasks.txt", "w")

            file.writelines(tasks)

            file.close()

            print("Task Deleted!")

        else:
            print("Invalid Task Number")

    elif choice == "4":

        print("Goodbye!")

        break

    else:

        print("Invalid Choice")
        