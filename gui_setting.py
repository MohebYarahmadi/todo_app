import FreeSimpleGUI as sg
import functions

# Global Settings
sg.theme('Dark')


# Components
label1 = sg.Text('Type in a to-do')
add_input_box = sg.InputText(key="todo", do_not_clear=False, size=47)
add_btn = sg.Button("Add")
list_box = sg.Listbox(values=functions._get_list(),
                    key='item_select',
                    bind_return_key=True,
                    size=[45, 10])
                    
edit_btn = sg.Button("Edit", disabled=True)
del_btn = sg.Button("Delete", disabled=True)

close_btn = sg.Exit()
help_btn = sg.Button("Help")


# Create Wrapper
layout= [
    [label1],
    [add_input_box, add_btn],
    [list_box, edit_btn],
    [help_btn, close_btn]
]
