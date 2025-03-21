prompt = "Command >> "
# todos = []

print(" Todo List Application ".center(50, '='))
print("You can manage your todo list by these commands:")
print("add show remove remove compeleted")
print("".center(50, '-'))

while True:
    command = input(prompt).lower().strip()
    
    match command:            
        case 'exit':
            break
            
        case 'add':
            todo = input("Add a task: ").strip() + '\n'

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
            
        case 'show':
            print(" Tasks ".center(50, '-'))

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            if len(todos) > 0:
                for index, item in enumerate(todos, start=1):
                    print(f"{index}: {item.title()}", end='')
            else:
                print("There is no task yet, type add to start adding.")
            print('-' * 50)
            
        case 'edit':
            # show_list()
            item_id = int(input("Enter the task number to edit: "))
            if item_id > len(todos):
                print("Task not exist, try again.")
            else:
                todos[item_id - 1] = input("Update: ") + '\n'

                file = open('files/todos.txt', 'w')
                file.writelines(todos)
                file.close()
                
                print(f"Task {item_id} updated.")

        case 'complete':
            item_id = int(input("Enter the task number to complete: "))
            if item_id > len(todos):
                print("Task not exist, try again.")
            else:
                todos.pop(item_id - 1)

                file = open('files/todos.txt', 'w')
                file.writelines(todos)
                file.close()
                
                print(f"Task completed.")

        case 'order':
            item_id = int(input("Enter current position: "))
            new_id = int(input("Enter new position: "))
            if item_id - 1 == new_id - 1:
                print("Same position.")
            else:
                item = todos.pop(item_id - 1)
                todos.insert(new_id - 1, item)

                file = open('files/todos.txt', 'w')
                file.writelines(todos)
                file.close()
                
                print("Task moved to new position.")
            

        case 'help':
            print(" Help ".center(50, '-'))
            print("The commands that you can enter to get things done are:")
            print("add\t\tto add a new task to the list.")
            print("edit\t\tto edit the existed task by it's number.")
            print("compelte\tset the selected task by it's number as completed." \
            "\n\t\tthe task will be remove from the list.")
            print("show\t\tshow the current not completed tasks.")
            print("exit\t\tto exit the program.")
            print("help\t\tto see this text.")
            print('-' * 50)
            
        case _:
            print("Command not exist. try again.")
            
