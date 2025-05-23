import serial
import pygame
import os

# Inicializa o mixer do pygame
pygame.mixer.init()

# Pasta onde estão os sons
PASTA_SONS = os.path.join(os.path.dirname(__file__), 'sons')

# Mapeamento de sons (ajuste conforme quiser)
sons = {
    "1": "Som_baleia.mp3",
    "2": "Som_cobra.mp3",
    "3": "Som_gato.mp3",
    "4": "Som_ovelha.mp3",
    "5": "Som_pintinho.mp3",
    "6": "Som_porco.mp3",
    "7": "Som_sapo.mp3",
    "8": "Som_tigre.mp3"
}

# Configuração da porta serial
porta_serial = 'COM5'  # Altere conforme necessário
baud_rate = 9600
ser = serial.Serial(porta_serial, baud_rate)

print(f'Conectado à {porta_serial}, aguardando comando...')

try:
    while True:
        if ser.in_waiting:
            linha = ser.readline().decode('utf-8').strip()
            print(f"Recebido: {linha}")

            if linha.startswith("COR:"):
                cor = linha.split(":")[1].strip()
                if cor in sons:
                    caminho_som = os.path.join(PASTA_SONS, sons[cor])
                    print(f"Tocando som: {caminho_som}")
                    pygame.mixer.music.load(caminho_som)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        continue
                else:
                    print("Cor recebida não está mapeada para nenhum som.")
except KeyboardInterrupt:
    print("Encerrando programa.")
finally:
    ser.close()
