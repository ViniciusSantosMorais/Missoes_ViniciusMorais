import cv2
imagem = cv2.imread('Gon.jpg')
for y in range(0, imagem.shape[0]):    #Percorre linhas
 for x in range(0, imagem.shape[1]):   #Percorre colunas
  imagem[y, x] = (x%256,y%256,x%256)   #Modificando as cores

cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
cv2.imwrite("coloridoGon.jpg", imagem)    #Salvando a imagem no disco
