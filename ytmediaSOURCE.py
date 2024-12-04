from pathlib import Path
import os
from pywebio.input import input, actions
from pywebio import start_server
from pywebio.output import put_text
from yt_dlp import YoutubeDL

user_profile_path = os.environ['USERPROFILE']
user_name = os.path.basename(user_profile_path)

def choose():
    action = actions(label="Escolha:", buttons=["MP3", "MP4"])
    if action == "MP3":
        mp3()
    elif action == "MP4":
        mp4()

def mp4():
    link = input("Coloque o link (MP4):", required=True)
    try:
        put_text("Baixando o vídeo...").style('color: red; font-size: 50px')

        ydl_opts = {"outtmpl": fr"C:\Users\{user_name}\Downloads\%(title)s.%(ext)s"}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        put_text("Download concluído com sucesso!").style('color: green; font-size: 50px')
    except Exception as e:
        put_text(f"Erro no download: {e}").style('color: red; font-size: 30px')

def mp3():
    link = input("Coloque o link (MP3):", required=True)
    try:
        put_text("Baixando o áudio...").style('color: red; font-size: 50px')

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': fr"C:\Users\{user_name}\Downloads\%(title)s.%(ext)s",
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        put_text("Download concluído com sucesso!").style('color: green; font-size: 50px')
    except Exception as e:
        put_text(f"Erro no download: {e}").style('color: red; font-size: 30px')

if __name__ == "__main__":
    choose()
