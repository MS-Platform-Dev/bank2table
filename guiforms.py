# Module to hold the UI forms

def gui_banner():
# Simple welcome page

    # Play/test code
    layout = [[sg.Text('Just a number')],
                     [sg.InputText()],
                     [sg.Submit(), sg.Cancel()]]
    window = sg.Window('Simple Number', layout)
    event, values = window.read()
    window.close()
    text_input = values[0]
    sg.popup('You entered', text_input)

