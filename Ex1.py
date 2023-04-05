import cv2 # Importação das bibliotecas

imagem = cv2.imread('Gon.jpg') # Leitura da imagem com a função imread
print('Largura em pixels: ', end='')
print(imagem.shape[1]) # Mostra a largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) # Mostra a altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])

cv2.imshow("Nome da janela", imagem) # Função imshow: mostra a imagem
cv2.waitKey(0)                       # espera pressionar qualquer tecla
cv2.imwrite("SaidaGon.jpg", imagem)  # Função imwrite: Salva a imagem no disco
