import apps
import PySimpleGUI as sg

#---------------------------------------------------------------------------------------------------------------------------------

layout = [
    [sg.Text('LINK:',background_color='dimgray'), sg.Input('', key='-LINK-'), sg.Button('VERIFICAR',key='-BUTTON-')],
    
    [sg.Text('TITLE:',visible=False,key='text1',background_color='dimgray'), sg.Text('', key='-TITLE-',visible=False)],
    
    [sg.Text('DESCRIPTION:',visible=False,key='text2',background_color='dimgray')],
    [sg.Multiline('', key='-DESCRIPTION-',visible=False,size=(50,10),expand_x=True)],

    [sg.Text('VIDEO',expand_x=True,background_color='dimgray',visible=False, key='text3'),
     sg.Combo(values=('360p','480p','720p'),key='-VIDEO-',size=10,visible=False),

            sg.Text(' ' * 30, justification='center', background_color='dimgray',visible=False,key='text0') ,

        sg.Text('AUDIO', expand_x=True, justification='right',visible=False, background_color='dimgray', key='text4'),
         sg.Combo(values=('Median Quality','High Quality'),key='-AUDIO-',visible=False)],
    
    [sg.Button('DOWNLOAD',expand_x=True,visible=False)],
]
#---------------------------------------------------------------------------------------------------------------------------------

sg.theme_background_color('dimgray')
sg.theme_text_element_background_color('black')

#---------------------------------------------------------------------------------------------------------------------------------

WINDOW = sg.Window('SnapTudo', layout=layout, icon='icon.ico',
                     font='Helvetica', button_color='red')

#---------------------------------------------------------------------------------------------------------------------------------

while True:
    event, values = WINDOW.read()

    if event == sg.WIN_CLOSED:
        break
    #--------------------------------------------------------------------------------------------------------------------------------

    if event == '-BUTTON-':
        try:
            WINDOW['text1'].Update(visible=True)
            WINDOW['text2'].Update(visible=True)

            INFORMAÇÕES = apps.videoInfo(values['-LINK-'])
            WINDOW['-TITLE-'].Update(INFORMAÇÕES['title'],visible=True)
            WINDOW['-DESCRIPTION-'].Update(INFORMAÇÕES['description'],visible=True)

            WINDOW['text3'].Update(visible=True)
            WINDOW['-VIDEO-'].Update(visible=True)
            WINDOW['text0'].Update(visible=True)
            WINDOW['text4'].Update(visible=True)
            WINDOW['-AUDIO-'].Update(visible=True)
            WINDOW['DOWNLOAD'].Update(visible=True)

        except:
            WINDOW['-DESCRIPTION-'].Update('ERRO! VERIFIQUE O LINK...', visible=True)
    #--------------------------------------------------------------------------------------------------------------------------------

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
#---------------------------------------------------------------------------------------------------------------------------------

WINDOW.close()