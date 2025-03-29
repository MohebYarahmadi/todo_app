import FreeSimpleGUI as sg

# Global Settings
sg.theme('Default1')


# Components
label = sg.Text('Type in a to-do')
add_input_box = sg.InputText(key="Add")
add_btn = sg.Submit()
close_btn = sg.Exit(key='Exit')
help_btn = sg.Button("Help", key='help')


# Create Wrapper
wrapper= [
    [label],
    [add_input_box, add_btn],
    [help_btn, close_btn]
]
