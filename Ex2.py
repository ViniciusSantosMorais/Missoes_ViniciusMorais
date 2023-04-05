import cv2
imagem = cv2.imread('Gon.jpg')           #Leitura da imagem
for y in range(0, imagem.shape[0]):      #Lendo cada pixel
 for x in range(0, imagem.shape[1]):
  imagem[y, x] = (0,255,0)               #Mudando cada pixel para verde
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
cv2.imwrite("verdeGon.jpg", imagem)         #Salvando a imagem no disco
