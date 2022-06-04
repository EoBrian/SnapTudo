import apps
import PySimpleGUI as sg


layout = [
    [sg.Text('LINK:'), sg.Input('', key='-LINK-'), sg.Button('VERIFICAR',key='-BUTTON-')],
    
    [sg.Text('TITLE:',visible=False,key='text1'), sg.Text('', key='-TITLE-',visible=False)],
    
    [sg.Text('DESCRIPTION:',visible=False,key='text2')],
    [sg.Multiline('', key='-DESCRIPTION-',visible=False,size=(50,10),expand_x=True)],

    [sg.Text('VIDEO',expand_x=True), sg.Combo(values=('360p','480p','720p'),key='-VIDEO-'),
        sg.Text('AUDIO',expand_x=True), sg.Combo(values=('Median Quality','High Quality'),key='-AUDIO-'),],
    
    [sg.Button('DOWNLOAD',expand_x=True)],
]

sg.theme('DarkRed1')

WINDOW = sg.Window('SnapTudo', layout=layout, icon= 'icon.ico')

while True:
    event, values = WINDOW.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON-':
        try:
            WINDOW['text1'].Update(visible=True)
            WINDOW['text2'].Update(visible=True)

            INFORMAÇÕES = apps.videoInfo(values['-LINK-'])
            WINDOW['-TITLE-'].Update(INFORMAÇÕES['title'],visible=True)
            WINDOW['-DESCRIPTION-'].Update(INFORMAÇÕES['description'],visible=True)

        except:
            WINDOW['-DESCRIPTION-'].Update('ERRO! VERIFIQUE O LINK...')

    if event == 'DOWNLOAD':
        try:
    
            if values['-VIDEO-'] == '360p':
                apps.videoDownload(values['-LINK-'],1)
            elif values['-VIDEO-'] == '480p':
                apps.videoDownload(values['-LINK-'],2)       
            elif values['-VIDEO-'] == '720p':
                try:
                        apps.videoDownload(values['-LINK-'],3)
                except:
                        apps.videoDownload(values['-LINK-'],2)
            
            elif values['-AUDIO-'] == 'Median Quality':
                apps.audioDownload(values['-LINK-'],2)
            elif values['-AUDIO-'] == 'High Quality':
                apps.audioDownload(values['-LINK-'],-1)

            for items in values:
                values[items] = None
        except:
            WINDOW['-DESCRIPTION-'].Update('ERRO! AO BAIXAR...', visible=True)

WINDOW.close()