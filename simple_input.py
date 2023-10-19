import PySimpleGUI as sg

layout = [  [sg.Text('Nome'), sg.Input(key='-Nome-')],
          [sg.Text('Email'), sg.Input(key='-Email-')],
          [sg.Text('Cidade e Estado'), sg.Input(key='-Cidade e Estado-')],
          [sg.Ok(), sg.Cancel()]]

Windown = sg.Window('simple Inputs', layout)

while True:
    event, values = Windown.read()
    if event == sg.WIN_CLOSED or event == 'cancel':
        Windown.close()          
        