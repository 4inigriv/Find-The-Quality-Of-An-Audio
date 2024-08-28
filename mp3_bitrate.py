# instalar no pc lib mutagen
from mutagen.mp3 import MP3

def get_mp3_bitrate(file_path):
    audio = MP3(file_path)
    bitrate = audio.info.bitrate
    return bitrate / 1000  # Converte de bps para kbps

file_path = #caminho do arquivo onde tem o audio em formato MP3
bitrate = get_mp3_bitrate(file_path)
print(f'O bitrate do arquivo é: {bitrate} kbps')