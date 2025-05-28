import serial
import pygame
import os
import time

# === Inicializa o mixer do pygame ===
pygame.mixer.init()

# === Pasta onde estão os sons ===
PASTA_SONS = r"C:\projetos\sons"

# === Mapeamento de sons ===
sons = {
    "1": "Som_cobra.mp3",
    "2": "Som_porco.mp3",
    "3": "Som_tigre.mp3",
    "4": "Som_baleia.mp3",
    "5": "Som_sapo.mp3",
    "6": "Som_gato.mp3",
    "7": "Som_ovelha.mp3",
    "8": "Som_pintinho.mp3"
}

# === Configuração da porta serial ===
porta_serial = 'COM5'  # ⚠️ Ajuste conforme sua porta (ex.: COM3, COM7)
baud_rate = 9600

try:
    ser = serial.Serial(porta_serial, baud_rate, timeout=1)
    print(f'✅ Conectado na porta {porta_serial}. Aguardando comandos...')
except Exception as e:
    print(f'❌ Erro ao abrir a porta {porta_serial}: {e}')
    exit()

# === Função para tocar som ===
def tocar_som(codigo):
    if codigo in sons:
        caminho = os.path.join(PASTA_SONS, sons[codigo])
        if os.path.exists(caminho):
            print(f"🔊 Tocando som: {caminho}")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(caminho)
            pygame.mixer.music.play()
        else:
            print(f"⚠️ Arquivo de som não encontrado: {caminho}")
    else:
        print(f"⚠️ Código '{codigo}' não mapeado para nenhum som.")

# === Loop Principal ===
try:
    while True:
        if ser.in_waiting:
            linha = ser.readline().decode('utf-8').strip()
            if linha:
                print(f"📥 Recebido: {linha}")

                if linha.startswith("COR:"):
                    cor = linha.split(":")[1].strip()
                    tocar_som(cor)

        time.sleep(0.05)  # Delay curto para não sobrecarregar CPU

except KeyboardInterrupt:
    print("\n🛑 Encerrando programa manualmente...")
finally:
    ser.close()
    print("🔌 Porta serial fechada.")
