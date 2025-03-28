import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
add_input_box = sg.InputText(tooltip='enter here')
edit_input_box = sg.InputText(tooltip='enter here')
add_btn = sg.Button("Add")
clear_btn = sg.Button("Clear")

wrapper= [
    [label],
    [add_input_box, add_btn],
    [edit_input_box, clear_btn]
]

window = sg.Window('Todo App', layout=wrapper)
window.read()
window.close()
