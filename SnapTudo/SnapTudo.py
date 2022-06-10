import apps
import PySimpleGUI as sg

sg.theme_background_color('#4b0082')
sg.theme_button_color('#9932cc')
sg.theme_text_color('black')
sg.theme_text_element_background_color('#9932cc')

#---------------------------------------------------------------------------------------------------------------------------------
#LAYOUT INICIAL
layout_started = [
    [sg.Text('LINK:', background_color='#4b0082'), sg.Input('', key='-LINK-'), sg.Button('VERIFICAR',key='-BUTTON-')],
    [sg.Text('INSIRA ALGUM LINK!', key='-ERRO_LINK-', visible=False, justification='center', expand_x=True, background_color='#4b0082')],
]
#---------------------------------------------------------------------------------------------------------------------------------
#INFORMAÇÕES SOBRE O VIDEO: TITULO, DURAÇÃO E DESCRIÇÃO
info_video = [
    [sg.Text('TITLE:'),
        sg.Text('', key='-TITLE-')],

    [sg.Text('LENGTH:'), sg.Text('',key='-LENGTH-')],

    [sg.Multiline('', key='-DESCRIPTION-',size=(60,10),expand_x=True)]
]

#OPÇÕES DE DOWNLOAD DO VIDEO
download_bar = [
    
    #VIDEO HIGH QUALITY
    [sg.Text('VIDEO',expand_x=True, background_color='blueviolet', text_color='red')],
    
    [sg.Text('High Quality')],
    [sg.Button('Download', key='-HIGH-'), sg.Text('',key='-720P-'), sg.Text('', key='-HIGHSIZE-')],
    
    #VIDEO BEST QUALITY
    [sg.Text('Best Quality')],
    [sg.Button('Download', key='-BEST-'), sg.Text('',key='-360P-'), sg.Text('', key='-BESTSIZE-')],
    
    [sg.HorizontalSeparator()],

    #AUDIO
    [sg.Text('AUDIO', expand_x=True, background_color='blueviolet', text_color='red')],
    [sg.Button('Download', key='-AUDIO-'), sg.Text('',key='-QUALITY-'), sg.Text('', key='-AUDIOSIZE-')],

    [sg.VPush()],

    #BARRA DE PROGRESSO
    [sg.ProgressBar(100, size=(20,20), expand_x=True, key='-PROGRESSBAR-')],

    [sg.Text('', visible=False, key='-COMPLETE-', expand_x=True, justification='center')],
]

#LAYOUT DAS INFORMAÇÕES ACIMA
layout = [
    layout_started,
    [sg.TabGroup([[
        sg.Tab('info', info_video, key='-INFO-', background_color='#9932cc'), sg.Tab('donload', download_bar, background_color='#9932cc')
    ]], selected_background_color='black', background_color='#4b0082')]
]

#---------------------------------------------------------------------------------------------------------------------------------
WINDOW = sg.Window('SnapTudo', layout=layout, font='DejaVu, 13', icon='icon.ico')

#---------------------------------------------------------------------------------------------------------------------------------
while True:
    event, values = WINDOW.read()

    if event == sg.WIN_CLOSED:
        break
    
    #--------------------------------------------------------------------------------------------------------------------------------
    if event == '-BUTTON-' or event == 'enter:13':
        try:
            WINDOW['-ERRO_LINK-'].update(visible=False)
            WINDOW['-COMPLETE-'].update(visible=False)
            WINDOW['-PROGRESSBAR-'].update(100)

            video_object = apps.video(values['-LINK-'])
            
            WINDOW['-TITLE-'].update(video_object.title)
            WINDOW['-DESCRIPTION-'].update(video_object.description)
            
            #DURAÇÃO DO VIDEO
            if (video_object.length / 60) < 60:
                WINDOW['-LENGTH-'].update(f'{round(video_object.length / 60,2)} minutos')
            else:
                WINDOW['-LENGTH-'].update(f'{round(video_object.length / 60,2)/60 :.2f} horas')
            
            #IFORMAÇÕES DE DOWNLOAD

            #720P
            WINDOW['-720P-'].update(video_object.streams.get_highest_resolution().resolution)
            WINDOW['-HIGHSIZE-'].update(f'{round(video_object.streams.get_highest_resolution().filesize / 1048576,1)} MB')
           
            #360P
            WINDOW['-360P-'].update(video_object.streams.get_lowest_resolution().resolution)
            WINDOW['-BESTSIZE-'].update(f'{round(video_object.streams.get_lowest_resolution().filesize / 1048576,1)} MB')
            
            #AUDIO
            WINDOW['-AUDIOSIZE-'].update(f'{round(video_object.streams.get_audio_only().filesize / 1048576,1)} MB')

            
        except:
            WINDOW['-ERRO_LINK-'].update(visible=True)

    #--------------------------------------------------------------------------------------------------------------------------------
   

    try:
        if event == '-HIGH-':
            apps.threadEls(apps.video_highest(video_object), 1)
            WINDOW['-PROGRESSBAR-'].update(100)
            apps.completeDownload(WINDOW, 'DOWNLOAD COMPLETO!')
        
        if event == '-BEST-':
            apps.threadEls(apps.video_lowest(video_object), 1)
            WINDOW['-PROGRESSBAR-'].update(100)
            apps.completeDownload(WINDOW, 'DOWNLOAD COMPLETO!')
        
        if event == '-AUDIO-':
            apps.threadEls(apps.audioDownload(video_object, -1), 1)
            WINDOW['-PROGRESSBAR-'].update(100)
            apps.completeDownload(WINDOW, 'DOWNLOAD COMPLETO!')
    except:
        apps.completeDownload(WINDOW, 'ERRO NO DOWNLOAD!')

#---------------------------------------------------------------------------------------------------------------------------------
WINDOW.close()