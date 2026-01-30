import cv2

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
        print("Não foi possível receber o frame (fim da transmissão?).")
        break

    # 3. Exibe o frame resultante em uma janela chamada 'Video'
    cv2.imshow('Video', frame)

    # 4. Loop de espera: verifica se a tecla 'q' foi pressionada para sair
    # O waitKey(1) espera 1ms entre frames para processar inputs
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. Libera a captura e fecha as janelas
video_capture.release()
cv2.destroyAllWindows()