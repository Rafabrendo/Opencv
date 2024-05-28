# IMPORT O OPENCV
import cv2

# ABRIR A IMAGEM
img = cv2.imread('Orange.png')

# DESENHANDO LINHA  
cv2.line(img,(100,10),(200,200),(0,255,0),5)
#começa com 10 de distancia da horizontal e 10 da vertical 
#e termina com 200 de distancia da horizontal e 200 da vertical
#dps vem cor e espessura

# DESENHAR RETANGULO
cv2.rectangle(img, (100,10),(200,200),(0,255,255),5)
# ponto inicial e final do retangulo, cor e espessura

cv2.rectangle(img, (200,10),(400,400),(0,255,255),-1)

# DESENHAR CIRCULO
cv2.circle(img, (200,200), 50, (255,0,255), 3)
# Onde começa, o tamanho do raio, a cor e a espessura

cv2.circle(img, (300,150), 50, (255,0,255), -1)
#para fazer um circulo todo preenchido

# DESENHAR TEXTO
cv2.putText(img, 'OpenCV', (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)

# EXIBIR A IMAGEM
cv2.imshow('img', img)

# PAUSA
cv2.waitKey(0)