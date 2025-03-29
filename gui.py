import functions

from gui_setting import *


window = sg.Window('Todo App', layout)

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)

    match event:
        case sg.WIN_CLOSED | 'Exit':
            break
        case 'Add':
            todos = functions._get_list()
            todos.append(values["todo"] + "\n")
            functions._post_list(todos)
            window['item_select'].update(values=todos)
            print('todo added')
            
        case 'item_select':
            window['todo'].update(value=values['item_select'][0])
            window['Edit'].update(disabled=False)
            
        case 'Edit':
            current_item = values['item_select'][0]
            new_item = values['todo']

            todos = functions._get_list()
            item_id = todos.index(current_item)
            todos[item_id] = new_item + '\n'
            functions._post_list(todos)
            window['item_select'].update(values=todos)
            window['Edit'].update(disabled=True)
            print('todo updated')
            
        case 'help':
            print('show help')

window.close()
