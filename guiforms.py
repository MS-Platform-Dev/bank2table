#-------------------------------------------------------------------------------
# Copyright ©2024 MonaCompta
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#-------------------------------------------------------------------------------

# Module:       guiforms.py
# Description:  Module to hold the UI forms

# Author:       Mike
# Copyright:    ©2024 MonaCompta
# Licence:      MIT

# Change Log:
# DATE          VERSION       DESCRIPTION
# 2022-04-18    0.1  alpha    Initial commit
# 2024-10-17    0.2  alpha    Add copyright banner
#-------------------------------------------------------------------------------


import PySimpleGUI as sg

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

    
def gui_settings():
    # TODO: Add UI to change permanent settings
    pass


def twonums():
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

def threenums():
    layout = [[sg.Text('Just a number')], 
              [sg.InputText()],
              [sg.InputText()],
              [sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Simple Number', layout)

    event, values = window.read()
    window.close()

    text_input1 = values[0]
    text_input2 = values[1]
    text_input3 = values[2]
    print(event)
    print(values)
    sg.popup('You entered', text_input1 + " " + text_input2 + " " + text_input3)

