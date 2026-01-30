import cv2

# Carrega o reconhecedor e o detector
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read('classificadorLBPH.yml') # Lê o "cérebro" que criamos
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Define os nomes (O ID 0 é vazio, o ID 1 é você)
# Se treinou mais pessoas (ID 2, 3...), adicione os nomes na lista
nomes = ['Ninguem', 'Leandro','Alex'] 

video_capture = cv2.VideoCapture(0)

print("Iniciando reconhecimento... Pressione 'q' para sair.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        # Aumentar um pouco o quadrado para o queixo (como fizemos antes)
        ajuste_queixo = 30
        cv2.rectangle(frame, (x, y), (x + w, y + h + ajuste_queixo), (0, 255, 0), 2)

        # O comando predict tenta adivinhar quem é
        # Ele retorna o ID (quem é) e a "confiança" (distância)
        id, confianca = reconhecedor.predict(gray[y:y+h, x:x+w])

        # Verificação da confiança
        # No LBPH, "0" é match perfeito.
        # Geralmente, abaixo de 50 ou 60 é um reconhecimento confiável.
        if confianca < 100:
            id_nome = nomes[id]
            confianca_texto = f"  {round(100 - confianca)}%"
        else:
            id_nome = "Desconhecido"
            confianca_texto = f"  {round(100 - confianca)}%"

        # Escreve o nome na tela (Acima do retângulo)
        cv2.putText(frame, str(id_nome), (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        # Escreve a porcentagem (Abaixo do nome)
        cv2.putText(frame, str(confianca_texto), (x + 5, y + h + ajuste_queixo - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)

    cv2.imshow('Reconhecimento Facial', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()