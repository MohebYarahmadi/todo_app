import os

prompt = "Command >> "
flag = True
# todos = []

print(" Todo List Cli Application ".center(50, '='))
print(" Moheb Yarahmadi ".center(50, '*'))
print("You can manage your todo list by these commands:")
print("add show remove remove compeleted")
print("".center(50, '-'))

while True:
    user_input = input(prompt).lower().strip()
    csp = user_input.find(' ')
    if csp == -1:
        command = user_input.strip()
        flag = False
    else:
        command = user_input[:csp].strip()
        flag = True

    match command:
        case 'quit' | 'exit':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saving...\nDone!")
            print(' Bye! '.center(50, '-'))
            break

        case 'add':
            os.system('cls' if os.name == 'nt' else 'clear')
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
            os.system('cls' if os.name == 'nt' else 'clear')
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
            os.system('cls' if os.name == 'nt' else 'clear')
            if flag:
                item_id = int(user_input[csp:].strip())
            else:
                print('Missing argument.  Type help to learn.')
                print(' Failed '.center(50, '-'))
                continue

            if item_id > len(todos):
                print('Out of range.')
                print(' Failed '.center(50, '-'))
            else:
                todos[item_id - 1] = input("Update: ") + '\n'

                with open('files/todos.txt', 'w') as file:
                    file.writelines(todos)

                print(f"Task {item_id} updated.")
                print(' Done '.center(50, '-'))

        case 'done':
            os.system('cls' if os.name == 'nt' else 'clear')
            if flag:
                item_id = int(user_input[csp:].strip())
            else:
                print('Missing argument.  Type help to learn.')
                print(' Failed '.center(50, '-'))
                continue
                
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
            os.system('cls' if os.name == 'nt' else 'clear')
            if flag:
                item_id = int(user_input[csp:].strip())
            else:
                print('Missing argument.  Type help to learn.')
                print(' Failed '.center(50, '-'))
                continue
                
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
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" Help ".center(50, '-'))
            print("List of the commands that you can use to get things done are:")
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
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Command not found.")
            print(' Failed '.center(50, '-'))
