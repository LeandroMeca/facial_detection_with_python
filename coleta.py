import cv2
import os

# Carrega o detector de faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Abre a câmera
video_capture = cv2.VideoCapture(0)

print("Olhe para a câmera e espere... Tirando fotos!")

# Contador de fotos tiradas
contagem = 0

# ID do usuário (1 = você). Se fosse outra pessoa, mudaria para 2, 3...
id_usuario = 1

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Converte para cinza (o reconhecimento aprende em preto e branco)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

    for (x, y, w, h) in faces:
        # Desenha o retângulo só para você ver que está funcionando
        cv2.rectangle(frame, (x, y), (x+w, y+h+30), (0, 255, 0), 2)

        # Incrementa o contador
        contagem += 1

        # Salva a imagem recortada na pasta 'fotos'
        # O nome do arquivo será: User.1.1.jpg, User.1.2.jpg, etc.
        nome_arquivo = f"fotos/User.{id_usuario}.{contagem}.jpg"
        
        # Recorta a imagem: pega do ponto y até y+h (altura) e x até x+w (largura)
        cv2.imwrite(nome_arquivo, gray_frame[y:y+h, x:x+w])

        print(f"Foto {contagem} capturada!")

    cv2.imshow('Coletando Dados', frame)

    # Para automaticamente depois de 30 fotos OU se apertar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q') or contagem >= 30:
        break

print("Coleta finalizada! Verifique a pasta 'fotos'.")
video_capture.release()
cv2.destroyAllWindows()