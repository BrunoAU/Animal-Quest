import os
import random
from playsound import playsound

# Caminho para a pasta de sons
PASTA_SONS =  #Caminho do arquivo com os sons

# Sons disponíveis (certifique-se de que os nomes estão corretos)
SONS_BOTOES = [
    ("azul",    "Som_baleia.mp3"),
    ("branco",  "Som_ovelha.mp3"),
    ("preto",   "Som_gato.mp3"),
    ("verde",   "Som_sapo.mp3"),
    ("amarelo", "Som_pintinho.mp3"),
    ("vermelho","Som_cobra.mp3"),
    ("laranja", "Som_tigre.mp3"),
    ("rosa",    "Som_porco.mp3"),
]

# Verifica se todos os arquivos existem e têm a extensão correta
def verificar_extensoes():
    for cor, arquivo in SONS_BOTOES:
        caminho = os.path.join(PASTA_SONS, arquivo)
        if not os.path.isfile(caminho):
            print(f"❌ Arquivo não encontrado: {caminho}")
        elif not arquivo.endswith(".mp3"):
            print(f"⚠ Arquivo com extensão incorreta: {arquivo}")
        else:
            print(f"✅ {arquivo} (ok)")

# Função para tocar o som
def tocar_som(arquivo):
    caminho = os.path.join(PASTA_SONS, arquivo)
    print(f"🔊 Tentando tocar som: {caminho}")
    try:
        playsound(caminho)
    except Exception as e:
        print(f"⚠ Erro ao tocar som: {e}")

# Função principal
def main():
    # Verifica se a pasta existe
    if not os.path.exists(PASTA_SONS):
        print(f"🚫 Pasta de sons não encontrada: {PASTA_SONS}")
        return

    # Verifica os arquivos antes de começar
    verificar_extensoes()

    # Escolhe um som aleatório
    botao_correto, arquivo_som = random.choice(SONS_BOTOES)
    print(f"🎯 O som correto é para o botão: {botao_correto}")
    tocar_som(arquivo_som)

    tentativas = 0
    acertou = False

    # Testa as tentativas
    while tentativas < 2 and not acertou:
        resposta = input("🎮 Pressione o botão (cor) que você acha que é o som: ").strip().lower()
        if resposta == botao_correto:
            print("🎉 Acertou!")
            acertou = True
        else:
            tentativas += 1
            print(f"❌ Errado! Tentativa {tentativas}/2")
            if tentativas < 2:
                print("🔁 Repetindo o som...")
                tocar_som(arquivo_som)
            else:
                print(f"💥 Fim das tentativas. O som era: {botao_correto}.")

# Executa o script
if __name__ == "__main__":
    main()
