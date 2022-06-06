from pytube import YouTube
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


def audioDownload(video_object, set_audio=-1):  
    video_object.streams.filter(only_audio=True)[set_audio].download(pathDir())
    renameAudio()

