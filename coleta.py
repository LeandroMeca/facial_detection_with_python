import cv2
import os

# Carrega o detector de faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# --- NOVO: Pergunta o ID no terminal antes de abrir a câmera ---
id_usuario = input('\nDigite o ID do usuário (1, 2, 3...): ')
print(f"Iniciando captura para o Usuário {id_usuario}. Olhe para a câmera!")

video_capture = cv2.VideoCapture(0)

contagem = 0

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        contagem += 1

        # Salva com o ID que você digitou
        nome_arquivo = f"fotos/User.{id_usuario}.{contagem}.jpg"
        cv2.imwrite(nome_arquivo, gray_frame[y:y+h, x:x+w])

        print(f"Foto {contagem} capturada para ID {id_usuario}!")

    cv2.imshow('Coletando Dados', frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or contagem >= 30:
        break

print("Coleta finalizada!")
video_capture.release()
cv2.destroyAllWindows()