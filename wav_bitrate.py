import wave

def obter_informacoes_audio(filepath):
    with wave.open(filepath, 'rb') as audio:
        taxa_amostragem = audio.getframerate()
        profundidade_bits = audio.getsampwidth() * 8  # Convertendo bytes para bits
        canais = audio.getnchannels()

        return taxa_amostragem, profundidade_bits, canais

def calcular_bitrate(filepath):
    taxa_amostragem, profundidade_bits, canais = obter_informacoes_audio(filepath)

    # Calcula a taxa de bits em bits por segundo
    bitrate = taxa_amostragem * profundidade_bits * canais

    # Converte para kilobits por segundo (kbps)
    bitrate_kbps = bitrate / 1000

    return bitrate_kbps

# Exemplo de uso
filepath = #caminho do arquivo onde tem o audio EM FORMATO WAV

bitrate_kbps = calcular_bitrate(filepath)
print(f"A taxa de bits do arquivo WAV é: {bitrate_kbps} kbps")
