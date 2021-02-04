import youtube_dl

#Pedimos la URL de input al usuario
input_url = str(input("Ingrese la URL del video que sea convertir: "))

#Obtenemos el titulo del video
video_info = youtube_dl.YoutubeDL().extract_info(url=input_url, download=False)
video_title = video_info['title']

path = '$HOME/musica/mp3/'

#Setear las opciones para la descarga del video
opciones = {
    'format': 'bestaudio/best',
    'outtmpl': f"{path}/{video_title}.mp3",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

#Descargamos el video
with youtube_dl.YoutubeDL(opciones) as ydl:
    ydl.download([input_url])