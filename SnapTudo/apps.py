from pytube import YouTube
from time import sleep
import os


def pathDir():
    #Pegado diretório padrão do usuário
    informações = os.environ
    usuário = informações['USERPROFILE']
    
    #pasta download
    return rf'{usuário}\Downloads'


def pathDownload(diretório):
    #navegando até a pasta download
    os.chdir(diretório)

    return os.listdir()


def renameAudio():
    dir = pathDir()
    path = pathDownload(dir)
    
    for archive in path:
        if '.webm' in archive or '.mp4' in archive:
            extension = archive.split('.')
            extension.pop()
            extension.append('.mp3')
            past = ''.join(extension)
            
            os.rename(archive, past)


def video(url):
    yt = YouTube(url)
    return yt


def videoInfo(url):
    yt = video(url)
    title = yt.title
    description = yt.description
    set_video = yt.streams.filter(progressive=True)
    set_audio = yt.streams.filter(only_audio=True)

    INFORMAÇÕES = {
        'title': title,
        'description': description,
        'set_video': set_video,
        'set_audio': set_audio,   
    }
    
    return INFORMAÇÕES


def videoDownload(url,set_video=1):
    yt = video(url)
    yt.streams.filter(progressive=True)[set_video].download(pathDir())


def audioDownload(url,set_audio=-1):  
    yt = video(url)
    yt.streams.filter(only_audio=True)[set_audio].download(pathDir())

    renameAudio()

