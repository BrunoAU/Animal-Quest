import serial
import pygame
import os
import time

# === Inicializa o mixer do pygame ===
pygame.mixer.init()

# === Pasta onde estão os sons ===
PASTA_SONS = os.path.join(os.path.dirname(__file__), 'sons')

# === Mapeamento de sons ===
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

# === Configuração da porta serial ===
porta_serial = 'COM5'  # ⚠️ Ajuste conforme sua porta
baud_rate = 9600

try:
    ser = serial.Serial(porta_serial, baud_rate, timeout=1)
    print(f'✅ Conectado à {porta_serial}, aguardando comandos...')
except Exception as e:
    print(f'❌ Erro ao conectar na porta {porta_serial}: {e}')
    exit()

# === Função para tocar som ===
def tocar_som(codigo):
    if codigo in sons:
        caminho_som = os.path.join(PASTA_SONS, sons[codigo])
        if os.path.exists(caminho_som):
            print(f"🔊 Tocando som: {caminho_som}")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(caminho_som)
            pygame.mixer.music.play()
        else:
            print(f"⚠️ Arquivo não encontrado: {caminho_som}")
    else:
        print("⚠️ Código não mapeado para som.")

# === Loop principal ===
try:
    while True:
        if ser.in_waiting:
            linha = ser.readline().decode('utf-8').strip()
            if linha:
                print(f"🎯 Recebido: {linha}")

                if linha.startswith("COR:"):
                    cor = linha.split(":")[1].strip()
                    tocar_som(cor)

        time.sleep(0.05)  # Pequeno delay para não sobrecarregar CPU

except KeyboardInterrupt:
    print("🛑 Encerrando programa manualmente.")
finally:
    ser.close()
    print("🔌 Porta serial fechada.")
