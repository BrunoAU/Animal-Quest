# Animal Quest

## 🎮 HOW-TO-USE

Neste repositório você vai aprender como fazer o seu próprio **Animal Quest**.

Antes de começar o Animal Quest haverá um **tutorial 100% digital** para explicar a dinâmica do jogo de forma leve e interativa.

Para iniciar o jogo, você deve apertar qualquer botão (**"Press any Button"**).

Ao começar o jogo, **três animais serão apresentados** em três telas diferentes. Um deles emitirar seu som. A partir disso, você deve relacionar o **som do animal** com o **animal correto** e selecionar o botão que tem a **cor que representa** esse animal.

O sistema permite **2 tentativas** para cada rodada:

* ✅ Se você **acertar**, uma imagem de **parabéns** é exibida em todas as telas.
* ❌ Se você **errar**, o **som é repetido** e você pode tentar novamente.

---

## 🐾 Jogo de Sons dos Animais por Cores

### 🎯 Objetivo

Adivinhar a **cor do botão** correspondente ao **som do animal** reproduzido. O jogador possui **2 tentativas** para acertar cada rodada.

---

## 🛠 Requisitos Técnicos

### 📌 Pré-requisitos

| Componente      | Especificação               | Observações                     |
| --------------- | --------------------------- | ------------------------------- |
| Python          | Versão 3.8+                 | Testado em 3.10.6               |
| Sistema         | Windows/macOS/Linux         |                                 |
| Espaço em disco | \~10MB (para arquivos .mp3) | Depende da qualidade dos áudios |
| Arduino IDE     | Recomendado 2.2.1+          | Para upload nos dispositivos    |

---

### 📚 Dependências

#### 📦 Bibliotecas Python Necessárias

```bash
pip install pyserial
pip install pygame
```
#### 📦 Bibliotecas Arduino Necessárias

```bash
<SPI.h>
<SD.h>
<Adafruit_GFX.h>
<MCUFRIEND_kbv.h>
```

---

## ⚙️ Arquitetura do Projeto

### 💻 Componentes e Comunicação

**Arduino Mega (Master):**

* Embaralha e seleciona 3 cores (representando animais).
* Escolhe 1 delas como "cor correta".
* Envia comandos seriais ('c', 'r', etc.) aos 3 Arduino Uno (Slaves).
* Informa ao código Python via Serial (COM5) qual foi a cor correta para reprodução do som.
* Lê o botão pressionado e verifica se foi o acerto.
* Envia 'z' (acerto) ou 'x' (erro final) aos Slaves.

**Arduino Uno (Slaves):**

* Recebem o comando serial e exibem a imagem correspondente (.BMP).
* Mostram a imagem de parabéns ou limpam a tela dependendo do comando ('z' ou 'x').

**Python:**

* Recebe o comando com a cor correta via serial ("COR\:x").
* Reproduz o som do animal correspondente usando `pygame`.

### 📂 Estrutura de Pastas

```
AnimalQuest/
├── sons/
│   ├── Som_baleia.mp3
│   ├── Som_cobra.mp3
│   ├── Som_gato.mp3
│   └── ... outros sons
├── arduino/
│   ├── master.ino
│   └── slave.ino
├── tocar_som.py
└── README.md
```

---

## 💡 Dicas

* ✅ Coloque os arquivos `.mp3` dentro da pasta `sons/` no mesmo nível que `tocar_som.py`.
* ✅ Certifique-se de usar **caminho absoluto ou raw string** em `PASTA_SONS` no Python.
* ✅ Use **botões com input\_pull-up** conectados aos pinos 31, 33, 35, 37, 39, 41, 43 e 45 do Mega.
* ✅ Mantenha os Arduinos conectados em portas diferentes da USB para evitar conflitos.

---

## 🚀 Como Rodar

1. **Conecte o Arduino Mega** (Master) na porta COM5.
2. **Conecte os 3 Arduino Uno** (Slaves) nos pinos TX1, TX2, TX3 do Mega.
3. **Insira o Cartão SD** com as imagens `.bmp` em cada Slave.
4. **Faça upload** do código `master.ino` no Mega.
5. **Faça upload** do código `slave.ino` nos 3 Unos.
6. **Execute o script Python**:

```bash
python tocar_som.py
```

7. **No Serial Monitor do Arduino**, siga as instruções para jogar.

---

## 🛠 IDEs recomendadas

| IDE         | Vantagens                      | Link                                           |
| ----------- | ------------------------------ | ---------------------------------------------- |
| VS Code     | Leve, com extensões Python     | [Download](https://code.visualstudio.com)      |
| Arduino IDE | Upload direto e Serial Monitor | [Download](https://www.arduino.cc/en/software) |

---
