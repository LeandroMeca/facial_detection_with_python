import cv2
import os
import numpy as np
from PIL import Image # Biblioteca para manipular imagens

# Cria o reconhecedor LBPH
reconhecedor = cv2.face.LBPHFaceRecognizer_create()

# Carrega o detector de rostos (apenas para garantir)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Função para ler as imagens da pasta e pegar os IDs
def get_imagens_e_ids(caminho):
    # Pega o caminho de todos os arquivos na pasta 'fotos'
    caminhos_imagem = [os.path.join(caminho, f) for f in os.listdir(caminho)]
    
    faces = []
    ids = []

    for caminho_imagem in caminhos_imagem:
        # Abre a imagem e converte para escala de cinza
        imagem_pil = Image.open(caminho_imagem).convert('L')
        
        # Converte a imagem em um array de números (matriz) que o OpenCV entende
        imagem_np = np.array(imagem_pil, 'uint8')

        # Pega o ID do usuário pelo nome do arquivo (User.1.5.jpg -> o ID é o 1)
        # O split separa por pontos e pega o índice 1
        id = int(os.path.split(caminho_imagem)[-1].split(".")[1])

        faces.append(imagem_np)
        ids.append(id)

    return faces, ids

print("Treinando o sistema... Aguarde.")

faces, ids = get_imagens_e_ids('fotos')

# --- O TREINAMENTO ACONTECE AQUI ---
reconhecedor.train(faces, np.array(ids))

# Salva o modelo treinado num arquivo
reconhecedor.write('classificadorLBPH.yml')

print(f"Treinamento concluído! {len(np.unique(ids))} rosto(s) aprendido(s).")
print("Arquivo 'classificadorLBPH.yml' foi criado.")