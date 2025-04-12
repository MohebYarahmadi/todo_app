import functions
import os

# import time


prompt = "Command >> "
flag = True

functions.banner(50)

while True:
    flag, user_input, command, csp = functions.parse_command(prompt)

    match command:
        case "quit" | "exit":
            print("Saving...\nDone!")
            print(" Bye! ".center(50, "-"))
            break

        case "add":
            #            date = time.strftime(" (%H:%M:%S)")
            #            todo = user_input[csp:].strip() + date + '\n'
            todo = user_input[csp:].strip() + "\n"

            todos = functions._get_list()

            todos.append(todo)

            functions._post_list(todos)

            print(" Done ".center(50, "-"))

        case "show" | "ls":
            functions._div("Tasks")

            todos = functions._get_list()

            # todos = [item.strip('\n') for item in todos]

            if len(todos) > 0:
                for index, item in enumerate(todos, start=1):
                    # item = item.strip('\n')
                    print(f"{index}. {item.capitalize()}", end="")
            else:
                print("There is no task yet, type add to start adding.")

            functions._div("End")

        case "edit":
            if flag:
                item_id = int(user_input[csp:].strip())
            else:
                print("Missing argument.  Type help to learn.")
                print(" Failed ".center(50, "-"))
                continue

            if item_id > len(todos):
                print("Out of range.")
                print(" Failed ".center(50, "-"))
            else:
                todos[item_id - 1] = input("Update: ") + "\n"

                functions._post_list(todos)

                print(f"Task {item_id} updated.")
                functions._div("Done")

        case "done":
            if flag:
                item_id = int(user_input[csp:].strip())
            else:
                print("Missing argument.  Type help to learn.")
                functions._div("Failed")
                continue

            if item_id > len(todos):
                print("Task not exist, check the entry.")
                functions._div("Failed")
            else:
                item = todos.pop(item_id - 1).strip("\n")

                functions._post_list(todos)

                print(f"Task '{item}' is completed.")
                functions._div("Done")

        case "order":
            if flag:
                item_id = int(user_input[csp:].strip())
            else:
                print("Missing argument.  Type help to learn.")
                print(" Failed ".center(50, "-"))
                continue

            new_id = int(input("Enter new position: "))
            if item_id - 1 == new_id - 1:
                print("Same position.")
                functions._div("Failed")
            elif item_id > len(todos) or new_id > len(todos):
                print(f"Position {new_id} not available.")
                functions._div("Failed")
            else:
                item = todos.pop(item_id - 1)
                todos.insert(new_id - 1, item)

                functions._post_list(todos)

                print(f"Task number {item_id} >> {new_id}.")
                functions._div("Done")

        case "help":
            functions._div("Help")
            print("List of the commands that you can use to get things done are:")
            print("add <string>\tto add a new task to the list.")
            print("edit <id>\tto edit the existed task by it's number.")
            print(
                "done <id>\tset the selected task as done."
                "\n\t\tthe task will be remove from the list."
            )
            print("order <id>\tAsk for <new position> to reorder,")
            print("show\tshow the current not completed tasks.")
            print("exit\tto exit the program.")
            print("help\tto see this text.")
            functions._div("End")

        case "cls" | "clear":
            os.system("cls" if os.name == "nt" else "clear")
            functions.banner(50)

        case _:
            print("Command not found.")
            functions._div("Failed")
