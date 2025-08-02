import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet: ")
input_box1 = sg.InputText(tooltip="feet")

label2 = sg.Text("Enter inches: ")
input_box2 = sg.InputText(tooltip="inches")

add_button = sg.Button("Convert")

window = sg.Window("Convert feet to meters",
                   [[label1, input_box1],
                    [label2, input_box2],
                    [add_button]])

event, values = window.read()
feet = values[0]
inches = values[1]

meters = feet/inches

print(event, values)
window.close()