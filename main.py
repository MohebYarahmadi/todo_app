import os

prompt = "Command >> "
flag = True
# todos = []

print(" Todo List Cli Application ".center(50, '='))
print("You can manage your todo list by these commands:")
print("add show remove remove compeleted")
print("".center(50, '-'))

def parse_command(prompt):
    """Parse user input into command and flags.
    
    Args:
        prompt (str): The input prompt to display to the user.
        
    Returns:
        tuple: A tuple containing:
            - has_flags (bool): True if input contains additional text after command
            - raw_input (str): Return the if there is no flag after command
            - command (str): The extracted command (first word) if flag provided
            - space_pos (int): Position of first space, or -1 if none
    """
    # Get and clean user input
    raw_input = input(prompt).lower().strip()
    
    # Find the first space character
    space_pos = _space_pos(raw_input)
    
    # Extract command and determine if flags exist
    if space_pos == -1:
        command = raw_input
        has_flags = False
    else:
        command = raw_input[:space_pos]
        has_flags = True
    
    return has_flags, raw_input, command, space_pos


def _space_pos(raw_input):
    return raw_input.find(' ')

def _get_list(filepath):
    """Read the textlines and return as a list.
    
    Args:
        path (str): The path to the text file.
        
    Returns:
        list: A list containing:
            - Lines of the text file
    """
    with open(filepath) as file:
        return file.readlines()
    

def _post_list(filepath, lst):
    """Write the provided list into a text file.
    
    Args:
        path (str): The path to the text file.
        lst (list): A list to write into a text file.
        
    Returns:
        void
    """
    with open(filepath, 'w') as file:
        file.writelines(lst)

while True:
    flag, user_input, command, csp= parse_command(prompt)

    match command:
        case 'quit' | 'exit':
            print("Saving...\nDone!")
            print(' Bye! '.center(50, '-'))
            break

        case 'add':
            todo = user_input[csp:].strip() + '\n'

            todos = _get_list('files/todos.txt')

            todos.append(todo)

            _post_list('files/todos.txt', todos)

            print(' Done '.center(50, '-'))

        case 'show' | 'ls':
            print(" Tasks ".center(50, '-'))

            todos = _get_list('files/todos.txt')

            # todos = [item.strip('\n') for item in todos]

            if len(todos) > 0:
                for index, item in enumerate(todos, start=1):
                    # item = item.strip('\n')
                    print(f"{index}. {item.capitalize()}", end='')
            else:
                print("There is no task yet, type add to start adding.")

            print(' End '.center(50, '-'))

        case 'edit':
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

                _post_list('files/todos.txt', todos)

                print(f"Task {item_id} updated.")
                print(' Done '.center(50, '-'))

        case 'done':
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

                _post_list('files/todos.txt', todos)

                print(f"Task '{item}' is completed.")
                print(' Done '.center(50, '-'))

        case 'order':
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

                _post_list('files/todos.txt', todos)

                print(f"Task number {item_id} >> {new_id}.")
                print(' Done '.center(50, '-'))

        case 'help':
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

        case 'cls' | 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(' Cli Todo '.center(50, '-'))

        case _:
            print("Command not found.")
            print(' Failed '.center(50, '-'))
