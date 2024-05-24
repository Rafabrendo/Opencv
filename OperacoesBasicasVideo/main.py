# IMPORTAR O OPENCV
import cv2

# CAPTURAR VIDEO
cap = cv2.VideoCapture(0)
#Se eu tivesse um video e quisesse manipula-lo:
#cap = cv2.VideoCapture('nome-do-vide.extensao')

# CRIAR LOOP INFINITO
while(True):
    
    # RECUPERAR FRAME
    ret, frame = cap.read()
    #ret (return - é uma variavel booleana)
    # SE TEM RETORNO, MOSTRA FRAME
    if ret:
        cv2.imshow('frame', frame)
        
        # IMAGEM REDIMENSIONADA
        imgresize = cv2.resize(frame, (400,400))
        
        # CRIAR ROI
        roi = frame[100:500, 200:600]
        
        # MOSTRAR ROI
        cv2.imshow('roi', roi)
        
        # MOSTRAR O IMGRESIZE
        cv2.imshow('imgresize', imgresize)
    
    # RECUPERA O BOTAÕ APERTADO   
    key = cv2.waitKey(30) #Onde eu controlo a velocidade dos videos
    
    if key == ord('q'):
        break
    
# LIBERA O CACHE DE CAP
cap.release()

# DESTROI TODAS AS JANELAS ABERTAS
cv2.destroyAllWindows()