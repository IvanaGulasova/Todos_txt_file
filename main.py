def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg ,filepath="todos.txt"):
    """ Write the to-do items list in the text line."""
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)


while True:
    choice = input("Type add, show, edit, complete or exit: ")
    choice = choice.strip()

    if choice.startswith("add") or choice.startswith("new"):
        todo = choice[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif choice.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos, 1):
            item = item.strip("\n")
            print(f"{index}-{item}")

    elif choice.startswith("edit"):
        try:
            number = int(choice[5:])
            number -= 1

            todos = get_todos()

            new_todos = input("Enter new todo: ")
            todos[number] = new_todos + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif choice.startswith("complete"):
        try:
            number = int(choice[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list.")

        except IndexError:
            print("There is no item with that number.")
            continue

    elif choice.startswith("exit") or choice.startswith("quit"):
        print("Bye!")
        break

    else:
        print("Incorrect input, try again.")