#-------------------------------------------------------------------------------
# Name:         gui_num
# Purpose:      Code sample - Get a number dialog
#-------------------------------------------------------------------------------

import PySimpleGUI as sg



layout = [[sg.Text('Just a number')],
                 [sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window('Simple Number', layout)

event, values = window.read()
window.close()

text_input = values[0]
sg.popup('You entered', text_input)

#

##layout = [[sg.Text('Just a number')],
##                 [sg.InputText(key='-IN1-')],
##                 [sg.InputText(key='-IN2-')],
##                 [sg.Submit(), sg.Cancel()]]

layout = [[sg.Text('Just a number')],
                 [sg.InputText()],
                 [sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window('Simple Number', layout)

event, values = window.read()
window.close()

text_input1 = values[0]
text_input2 = values[1]
print(event)
print(values)
sg.popup('You entered', text_input1 + " " + text_input2)



def main():
    pass

if __name__ == '__main__':
    main()
