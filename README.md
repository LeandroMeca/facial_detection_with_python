<h1>Projeto de Reconhecimento Facial com Python e OpenCV</h1>

<p>Este projeto implementa um sistema completo de detecção e reconhecimento facial utilizando a biblioteca OpenCV. O sistema utiliza algoritmos Haar Cascade para detecção e LBPH (Local Binary Patterns Histograms) para o treinamento e identificação de usuários.</p>

<h2>📋 Pré-requisitos e Tecnologias</h2>

<p>Para executar este projeto, foi utilizado o <strong>VS Code</strong> com um ambiente virtual (venv). As principais tecnologias são:</p>
<p>- Python 3.x</p>
<p>- OpenCV (cv2)</p>
<p>- Pillow (PIL) para processamento de imagens</p>
<p>- Haar Cascade (haarcascade_frontalface_default.xml)</p>

<h2>📂 Hierarquia e Estrutura dos Arquivos</h2>

<p>Abaixo está a descrição de cada arquivo e sua função na ordem de execução do projeto:</p>

<h2>1. Coleta de Dados (coleta.py)</h2>
<p>Este é o primeiro passo. O script abre a webcam, detecta o rosto do usuário e salva 30 amostras na pasta 'fotos'.</p>
<p><strong>Funcionalidade:</strong> Solicita um ID numérico para o usuário e cria um banco de dados de imagens em escala de cinza.</p>

<h2>2. Treinamento da IA (treinamento.py)</h2>
<p>Este script processa as imagens coletadas. Ele lê a pasta 'fotos', associa as imagens aos IDs e treina o reconhecedor LBPH.</p>
<p><strong>Saída:</strong> Gera o arquivo <code>classificadorLBPH.yml</code>, que atua como o "cérebro" do sistema.</p>

<h2>3. Reconhecimento Final (reconhecedor_final.py)</h2>
<p>O script principal. Ele utiliza o modelo treinado para identificar rostos em tempo real via webcam.</p>
<p><strong>Funcionalidade:</strong> Desenha um retângulo no rosto, exibe o nome do usuário identificado e a porcentagem de confiança.</p>

<h2>4. Arquivos de Sistema</h2>
<p><strong>haarcascade_frontalface_default.xml:</strong> Modelo pré-treinado pelo OpenCV para detectar onde existe um rosto na imagem.</p>
<p><strong>classificadorLBPH.yml:</strong> Arquivo gerado pelo script de treinamento contendo os dados biométricos dos usuários cadastrados.</p>

<h2>🚀 Como Executar (Passo a Passo)</h2>

<p><strong>Passo 1:</strong> Ative seu ambiente virtual e instale as dependências:</p>
<p><code>pip install opencv-python opencv-contrib-python pillow</code></p>

<p><strong>Passo 2:</strong> Execute a coleta para cadastrar um rosto (defina o ID 1):</p>
<p><code>python coleta.py</code></p>

<p><strong>Passo 3:</strong> Treine o modelo com as fotos capturadas:</p>
<p><code>python treinamento.py</code></p>

<p><strong>Passo 4:</strong> Inicie o reconhecimento facial:</p>
<p><code>python reconhecedor_final.py</code></p>
