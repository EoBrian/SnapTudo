import apps
import PySimpleGUI as sg

#---------------------------------------------------------------------------------------------------------------------------------
#INFORMAÇÕES SOBRE O VIDEO: TITULO E DESCRIÇÃO
info_video = [
    [sg.Text('TITLE:',key='text1'),
        sg.Text('', key='-TITLE-',text_color='black')],

    [sg.Text('LENGTH:'), sg.Text('',key='-LENGTH-')],

    [sg.Text('DESCRIPTION:',key='text2')],
    [sg.Multiline('', key='-DESCRIPTION-',size=(50,10),expand_x=True)]
]

#OPÇÕES DE DOWNLOAD DO VIDEO
download_bar = [
    [sg.Text('VIDEO',expand_x=True, key='text3')],
    [sg.Text('High Quality')],
    [sg.Button('Download', key='-HIGH-'), sg.Text('',key='-QUALITY-'), sg.Text('', key='-SIZE-')],
    
    [sg.Text('Best Quality')],
    [sg.Button('Download', key='-BEST-'), sg.Text('',key='-QUALITY1-'), sg.Text('', key='-SIZE1-')],
    
    [sg.Text('AUDIO')],
    [sg.Button('Download', key='-AUDIO-'), sg.Text('',key='-QUALITY2-'), sg.Text('', key='-SIZE2-')],

]

#BARRA DE PROGRESSO
progressbar = [sg.ProgressBar(100, size=(20,20), expand_x=True, key='-PROGRESSBAR-')]

#LAYOUT DAS INFORMAÇÕES ACIMA
layout = [
    [sg.TabGroup([[
        sg.Tab('info', info_video, key='-INFO-'), sg.Tab('donload', download_bar)
    ]])]
]

#---------------------------------------------------------------------------------------------------------------------------------
#LAYOUT INICIAL
layout_started = [
    [sg.Text('LINK:'), sg.Input('', key='-LINK-'), sg.Button('VERIFICAR',key='-BUTTON-')],
    [sg.Text('INSIRA ALGUM LINK!', key='-ERRO_LINK-', visible=False, justification='center', expand_x=True)],
]

#---------------------------------------------------------------------------------------------------------------------------------
sg.theme('Darkred1')

#---------------------------------------------------------------------------------------------------------------------------------
WINDOW = sg.Window('SnapTudo', layout=layout_started)

#---------------------------------------------------------------------------------------------------------------------------------
while True:
    event, values = WINDOW.read()

    if event == sg.WIN_CLOSED:
        break

    #--------------------------------------------------------------------------------------------------------------------------------
    if event == '-BUTTON-':
        try:
            video_object = apps.video(values['-LINK-'])
            WINDOW.close()

            WINDOW = sg.Window('SnapTudo', layout=layout, finalize=True)
            WINDOW['-TITLE-'].update(video_object.title)
            WINDOW['-DESCRIPTION-'].update(video_object.description)
            
            if (video_object.length / 60) < 60:
                WINDOW['-LENGTH-'].update(f'{round(video_object.length / 60,2)} minutos')
            else:
                WINDOW['-LENGTH-'].update(f'{round(video_object.length / 60,2)/60 :.2f} horas')

        except:
            WINDOW['-ERRO_LINK-'].update(visible=True)
    #--------------------------------------------------------------------------------------------------------------------------------
    if event == 'DOWNLOAD':
    
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

#---------------------------------------------------------------------------------------------------------------------------------
WINDOW.close()