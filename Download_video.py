from pytube import YouTube


def download_video(url, path_save=None):
    yt = YouTube(url).streams.get_highest_resolution()

    return yt.download()


def show_info_video(url):
    yt = YouTube(url)
    print("Título do vídeo: ", yt.title)
    print("Quantidade de visualizações do vídeo: ", yt.views)
    print("Duração do vídeo em segundos: ", yt.length)


def convert_to_mp3(path):
    with open(path, 'rb') as file:
        reader = file.read()
        with open(path.replace(".mp4", ".mp3"), 'wb') as nfile:
            nfile.write(reader)


show_info_video("https://www.youtube.com/watch?v=vNK58tL6J70")
