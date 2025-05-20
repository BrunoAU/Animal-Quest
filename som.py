import os
import random
import pygame

# Caminho para a pasta onde estão os arquivos de som
PASTA_SONS = r"C:\Users\nlpsl\Downloads\Sons"

# Sons disponíveis: (cor, nome do arquivo de som)
SONS_BOTOES = [
    ("azul", "Som_baleia.mp3"),
    ("branco", "Som_ovelha.mp3"),
    ("preto", "Som_gato.mp3"),
    ("verde", "Som_sapo.mp3"),
    ("amarelo", "Som_pintinho.mp3"),
    ("vermelho", "Som_cobra.mp3"),
    ("laranja", "Som_tigre.mp3"),
    ("rosa", "Som_porco.mp3")
]

# Verifica se todos os arquivos existem e têm a extensão correta
def verificar_extensoes():
    for cor, arquivo in SONS_BOTOES:
        caminho_arquivo = os.path.join(PASTA_SONS, arquivo)
        if not os.path.exists(caminho_arquivo):
            print(f"❌ Arquivo não encontrado: {caminho_arquivo}")
        elif not arquivo.endswith(".mp3"):
            print(f"⚠️ Arquivo com extensão incorreta: {arquivo}")
        else:
            print(f"✅ {arquivo} (ok)")


# Função para tocar o som usando pygame
def tocar_som(arquivo):
    caminho = os.path.join(PASTA_SONS, arquivo)
    print(f"🔊 Tentando tocar som: {caminho}")
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue  # Espera o som terminar
    except Exception as e:
        print(f"⚠️ Erro ao tocar som: {e}")

# Programa principal (exemplo simples de teste)
if __name__ == "__main__":
    pygame.init()
    verificar_extensoes()

    # Escolhe um som aleatório
    cor_correta, som_correto = random.choice(SONS_BOTOES)
    print(f"\n🧠 O som correto é para o botão: {cor_correta}")

    tentativas = 0
    while tentativas < 3:
        print(f"\n🎵 Reproduzindo o som... Tentativa {tentativas + 1}")
        tocar_som(som_correto)

        resposta = input("👉 Pressione o botão (cor) que você acha que é o som: ").strip().lower()
        if resposta == cor_correta:
            print("✅ Acertou!")
            break
        else:
            print("❌ Errado!")
            tentativas += 1

    if tentativas == 3:
        print(f"😢 Você errou. A resposta correta era: {cor_correta}")
