# IMPORTANDO O OPENCV
import cv2

# ABRIR A IMAGEM
img = cv2.imread('Orange.png')

# MOSTRAR IMAGEM
cv2.imshow('image', img) #Vai mostrar a imagem

#SALVAR NOVA IMAGEM
cv2.imwrite('nova.png', img)

# CRIAR ROI
roi = img[75:250, 100:300]

# MOSTRAR ROI
cv2.imshow('ROI', roi)

# IMAGEM REDIMENSIONADA
imgresize  = cv2.resize(img, (600,600))

# MOSTRAR imgresize
cv2.imshow('imgresize', imgresize)

# PAUSA
cv2.waitKey(0)