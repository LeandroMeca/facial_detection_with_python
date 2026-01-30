import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 1. Inicializa a captura de vídeo. 
# O argumento '0' define a câmera padrão do computador/notebook.
video_capture = cv2.VideoCapture(0)

# Verificação de segurança: checa se a câmera abriu corretamente
if not video_capture.isOpened():
    print("Erro: Não foi possível acessar a câmera.")
    exit()

print("Câmera aberta! Pressione 'q' para sair.")

while True:
    # 2. Captura frame a frame
    # 'ret' é um booleano (True se funcionou), 'frame' é a imagem capturada
    ret, frame = video_capture.read()

    if not ret:
        break

    # --- NOVO: Converter para Escala de Cinza ---
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # --- NOVO: Detectar os rostos ---
    # scaleFactor=1.1: Reduz a imagem em 10% a cada escala para achar rostos de tamanhos diferentes
    # minNeighbors=5: Quantidade de vizinhos para validar que é um rosto (evita falsos positivos)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    # --- NOVO: Desenhar o retângulo ao redor de cada rosto detectado ---
    # (x, y) é o ponto inicial, (w, h) são largura e altura
    for (x, y, w, h) in faces:

        ajuste_queixo=30

        # Desenha um retângulo VERDE (0, 255, 0) com espessura 2 na imagem ORIGINAL (colorida)
        cv2.rectangle(frame, (x, y), (x+w, y+h+ajuste_queixo), (0, 255, 0), 2)


    # 3. Exibe o frame resultante em uma janela chamada 'Video'
    cv2.imshow('Video', frame)

    # 4. Loop de espera: verifica se a tecla 'q' foi pressionada para sair
    # O waitKey(1) espera 1ms entre frames para processar inputs
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. Libera a captura e fecha as janelas
video_capture.release()
cv2.destroyAllWindows()