import functions

from gui_setting import *


window = sg.Window('Todo App',
                    layout=wrapper,
                    font=('JetBrains Mono', 10)
                    )

while True:
    event, values = window.read()
    print(event)

    match event:
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
        case 'Submit':
            print('adding todo')
            todos = functions._get_list()
            todos.append(values["Add"] + "\n")
            functions._post_list(todos)
        case 'help':
            print('show help')

window.close()
