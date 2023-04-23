while True:
    choice = input("Type add, show, edit, complete or exit: ")
    choice = choice.strip()

    if choice.startswith("add") or choice.startswith("new"):
        todo = choice[4:]
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("todos.txt", "w", encoding="utf-8") as file:
            file.writelines(todos)

    elif choice.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos, 1):
            item = item.strip("\n")
            print(f"{index}-{item}")

    elif choice.startswith("edit"):
        try:
            number = int(choice[5:])
            number -= 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todos = input("Enter new todo: ")
            todos[number] = new_todos + "\n"

            with open("todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif choice.startswith("complete"):
        try:
            number = int(choice[9:])

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list.")

        except IndexError:
            print("There is no item with that number.")
            continue

    elif choice.startswith("exit") or choice.startswith("quit"):
        print("Bye!")
        break

    else:
        print("Incorrect input, try again.")