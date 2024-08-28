
# Qualidade-Audio

Este projeto fornece uma ferramenta para avaliar a qualidade de arquivos de áudio com base em sua taxa de bits, retornando essa informação em kbps (kilobits por segundo).

## Como a "Qualidade" de um Áudio MP3 Funciona

A qualidade dos arquivos MP3 é geralmente determinada pela taxa de bits (bitrate), que mede a quantidade de dados processados por segundo. A taxa de bits é um fator chave na definição da qualidade sonora do arquivo:

- **128 kbps:** Considerado de baixa qualidade, com perda perceptível na clareza do áudio.
- **320 kbps:** Considerado de alta qualidade, com uma reprodução sonora mais próxima do original, mantendo detalhes e nuances.

## Como a "Qualidade" de um Áudio WAV Funciona

Diferente do MP3, que é um formato de compressão com perda, o WAV é um formato de áudio sem compressão, mantendo a qualidade original do som. A qualidade de um arquivo WAV não é medida pela taxa de bits, mas sim pela **taxa de amostragem** (sampling rate) e pela **profundidade de bits** (bit depth). 

- **Taxa de amostragem:** Geralmente 44.1 kHz, que significa que o áudio é amostrado 44.100 vezes por segundo.
- **Profundidade de bits:** Normalmente 16 bits, o que define a precisão de cada amostra.

Para calcular a taxa de bits, pode usar a fórmula frequência de amostragem * profundidade de bits * Nº de canais. 
