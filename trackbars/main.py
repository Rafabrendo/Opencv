# IMPORT O OPENCV
import cv2

# FUNCOES
def nothing(x):
    pass

# CRIAR JANELAS DE TRACKBARS
cv2.namedWindow('trackbars')

# CRIAR AS TRACKBARS
# primeiro parametro: nome da trackbar
# onde vai ser criada
# valores min(começa) e maximo
# função callback
cv2.createTrackbar('x', 'trackbars', 0, 800, nothing)
cv2.createTrackbar('y', 'trackbars', 0, 800, nothing)
cv2.createTrackbar('w', 'trackbars', 100, 800, nothing)
cv2.createTrackbar('h', 'trackbars', 100, 800, nothing)
# w -> width
# h -> height


# CAPTURAR VIDEO
cap = cv2.VideoCapture(0)

# LOOP INFINITO 
while(True):
    
    # RECUPERAR TRACKBAR
    x = cv2.getTrackbarPos('x', 'trackbars')
    y = cv2.getTrackbarPos('y', 'trackbars')
    w = cv2.getTrackbarPos('w', 'trackbars')
    h = cv2.getTrackbarPos('h', 'trackbars')
    
    # RECUPERAR O FRAME DO VIDEO
    ret, frame = cap.read()
    
    # CRIAR ROI
    roi = frame[y:h, x:w]
    
    # EXIBINDO O ROI
    cv2.imshow('roi', roi)
    
    #EXIBINDO O FRAME
    cv2.imshow('frame', frame)
    
    # PAUSA
    if cv2.waitKey(1) == ord('q'):
        break

# LIBERO O CAP
cap.release()

# DESTRUO TODAS AS JANELAS
cv2.destroyAllWindows
    