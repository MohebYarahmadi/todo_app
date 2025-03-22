prompt = "Command >> "
# todos = []

print(" Todo List Application ".center(50, '='))
print("You can manage your todo list by these commands:")
print("add show remove remove compeleted")
print("".center(50, '-'))

while True:
    user_input = input(prompt).lower().strip()
    csp = user_input.find(' ')
    if csp == -1:
        command = user_input.strip()
    else:
        command = user_input[:csp].strip()

    match command:
        case 'quit' | 'exit':
            print("Saving... done!")
            break

        case 'add':
            # todo = input("Add a task: ").strip() + '\n'
            # print('debug: add command')
            todo = user_input[csp:].strip() + '\n'

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            print(' Done '.center(50, '-'))

        case 'show':
            print(" Tasks ".center(50, '-'))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # todos = [item.strip('\n') for item in todos]

            if len(todos) > 0:
                for index, item in enumerate(todos, start=1):
                    # item = item.strip('\n')
                    print(f"{index}. {item.capitalize()}", end='')
            else:
                print("There is no task yet, type add to start adding.")

            print(' End '.center(50, '-'))

        case 'edit':
            # show_list()
            # item_id = int(input("Enter the task number to edit: "))
            item_id = int(user_input[csp:].strip())

            if item_id > len(todos):
                print(' Failed '.center(50, '-'))
            else:
                todos[item_id - 1] = input("Update: ") + '\n'

                with open('files/todos.txt', 'w') as file:
                    file.writelines(todos)

                print(f"Task {item_id} updated.")
                print(' Done '.center(50, '-'))

        case 'done':
            item_id = int(user_input[csp:].strip())
            if item_id > len(todos):
                print("Task not exist, check the entry.")
                print(' Failed '.center(50, '-'))
            else:
                item = todos.pop(item_id - 1).strip('\n')

                with open('files/todos.txt', 'w') as file:
                    file.writelines(todos)

                print(f"Task '{item}' is completed.")
                print(' Done '.center(50, '-'))

        case 'order':
            item_id = int(user_input[csp:].strip())
            new_id = int(input("Enter new position: "))
            if item_id - 1 == new_id - 1:
                print("Same position.")
                print(' Failed '.center(50, '-'))
            elif item_id > len(todos) or new_id > len(todos):
                print("Task not found.")
                print(' Failed '.center(50, '-'))
            else:
                item = todos.pop(item_id - 1)
                todos.insert(new_id - 1, item)

                with open('files/todos.txt', 'w') as file:
                    file.writelines(todos)

                print(f"Task number {item_id} >> {new_id}.")
                print(' Done '.center(50, '-'))

        case 'help':
            print(" Help ".center(50, '-'))
            print("The commands that you can enter to get things done are:")
            print("add <string>\tto add a new task to the list.")
            print("edit <id>\tto edit the existed task by it's number.")
            print("done <id>\tset the selected task as done."
                "\n\t\tthe task will be remove from the list.")
            print("order <id>\tAsk for <new position> to reorder the selected task.")
            print("show\tshow the current not completed tasks.")
            print("exit\tto exit the program.")
            print("help\tto see this text.")
            print('-' * 50)

        case _:
            print("Command not found. type 'help' to learn.")
            print(' Failed '.center(50, '-'))

print(' Bye! '.center(50, '-'))
