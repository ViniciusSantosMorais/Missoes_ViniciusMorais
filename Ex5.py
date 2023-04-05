import cv2
imagem = cv2.imread('Killua.jpg')
for y in range(0, imagem.shape[0], 10):   #Esta linha de código faz com que solte a cada 10 pixels ao percorrer as linhas
 for x in range(0, imagem.shape[1], 10):  #E mais 10 pixels ao percorrer as colunas.
  imagem[y:y+5, x: x+5] = (0,255,0)       #A cada salto é criado um quadrado verde de 5x5 pixels.

cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
cv2.imwrite("saidaKillua.jpg", imagem)    #Salvando a imagem no disco
