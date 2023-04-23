while True:
    choice = input("Type add, show, edit, complete or exit: ")
    choice = choice.strip()

    if "add" in choice or "new" in choice:
        todo = choice[4:]
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w", encoding="utf-8") as file:
            file.writelines(todos)
            file.writelines("\n")

    elif "show" in choice:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos, 1):
            item = item.strip("\n")
            print(f"{index}-{item}")

    elif "edit" in choice:
        number = int(choice[5:])
        number -= 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todos = input("Enter new todo: ")
        todos[number] = new_todos + "\n"

        with open("todos.txt", "w", encoding="utf-8") as file:
            file.writelines(todos)

    elif "complete" in choice:
        number = int(choice[9:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("todos.txt", "w", encoding="utf-8") as file:
            file.writelines(todos)

        print(f"Todo '{todo_to_remove}' was removed from the list.")

    elif "exit" in choice or "quit" in choice:
        print("Bye!")
        break

    else:
        print("Incorrect input, try again.")