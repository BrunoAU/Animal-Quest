# Animal Quest

## HOW-TO-USE

Neste repositório você vai aprender sobre como fazer o seu próprio **Animal Quest**.

Antes de começar o **Animal Quest** haverá um tutorial 100% digital para explicar a dinâmica do jogo de forma leve e interativa.

Para iniciar o jogo, você deve apertar qualquer botão ("Press any Button").

Ao começar o jogo, quatro animais serão apresentados e um deles emitirá seu som. A partir disso, você deve relacionar o som do animal com o animal correto e selecionar o botão que tem a cor que representa o animal que emitiu o som.

Em seguida, será emitida uma mensagem dependendo do resultado que você alcançou:

- Se você **acertar**, será exibida uma mensagem de **reforço positivo**.
- Se você **errar**, o som será repetido, e você deverá repensar qual escolha fazer com base na repetição do som do animal.

Assim, você seguirá até o final do jogo.



# 🐾 Jogo de Sons dos Animais por Cores

## � Objetivo
Adivinhar a cor do botão correspondente ao som de animal reproduzido. O jogador possui **2 tentativas** para acertar cada rodada.

## 🛠 Requisitos Técnicos

### 📋 Pré-requisitos
| Componente       | Especificação               | Observações                          |
|------------------|-----------------------------|--------------------------------------|
| Python           | Versão 3.8+                 | Testado em 3.10.6                    |
| Sistema          | Windows/macOS/Linux         |                                      |
| Espaço em disco  | ~10MB (para arquivos .mp3)  | Depende da qualidade dos áudios      |

## 📚 Dependências

### 📦 Bibliotecas Principais
python

import os          # Manipulação de arquivos
import random      # Seleção aleatória
from playsound import playsound  # Reprodutor de áudio

# Instalação básica
pip install playsound==1.2.2  # Windows

# Alternativas para outros SOs:
pip install pygame    # macOS/Linux
# ou
pip install simpleaudio

IDE	Vantagens	Link
VS Code	Leve e configurável	Download
