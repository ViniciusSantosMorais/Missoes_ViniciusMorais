import cv2
imagem = cv2.imread('Killua.jpg')
for y in range(0, imagem.shape[0], 1):   #Percorre as linhas
 for x in range(0, imagem.shape[1], 1):  #Percorre as colunas
  imagem[y, x] = (0,0,(x*y)%256)          #Alterando a cor
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

cv2.imwrite("saidaKillua.jpg", imagem)       #Salvando a imagem no disco
