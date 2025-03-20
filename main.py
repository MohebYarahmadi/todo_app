# from rich.console import Console
# from rich.prompt import Prompt
# console = Console()

prompt = "Command >> "
todos = []

print(" Todo List Application ".center(50, '='))
print("You can manage your todo list by these commands:")
print("add show remove remove compeleted")
# console.print("Set your todo-list items and don't break chain.", style="bold green")
print("".center(50, '-'))

while True:
    command = input(prompt).lower().strip()
    # command = Prompt.ask("Commands", choices=["add", "show", "update", "exit"])
    
    match command:
        # case '':
            # show_list()
            
        case 'exit':
            break
            
        case 'add':
            todo = input("Add a task: ")
            todos.append(todo)
            
        case 'show':
            counter = 1
            print(' Your List '.center(50, '-'))
            for todo in todos:
                print(counter, todo.capitalize())
                counter += 1
            print('-' * 50)
            
        case 'edit':
            # show_list()
            task_id = int(input("Enter the task number to edit: "))
            if task_id > len(todos):
                print("Task not exist, try again.")
            else:
                todos[task_id - 1] = input("Update: ")
                # todos.__setitem__(task_id - 1, input("new: "))
                print(f"Task {task_id} updated.")
            
        case _:
            print("Command not exist. try again.")
            
