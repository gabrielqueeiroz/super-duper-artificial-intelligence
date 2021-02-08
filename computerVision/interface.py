import tkinter as tk
import cv2
import random

def webcam():
    video = cv2.VideoCapture(0)
    classificador = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt.xml')

    while True:
        conectado, frame = video.read()
        # print(conectado)
        # print(frame)

        frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        facesDetectadas = classificador.detectMultiScale(frameCinza, minSize=(70, 70))
        for (x, y, l, a) in facesDetectadas:
            cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 0, 255), 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

def face():
    classificador = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt.xml')
    #classificador = cv2.CascadeClassifier('cascades/haarcascade_frontalcatface.xml')
    #classificador = cv2.CascadeClassifier('cascades/cars.xml')
    #classificador = cv2.CascadeClassifier('cascades/relogios.xml')

    fotos = ['pessoas/j.jpg', 'pessoas/k.jpg','pessoas/fed.jpg','pessoas/h.jpg','pessoas/abc.jpg', 'pessoas/def.jpg', 'pessoas/cba.jpg', 'pessoas/beatles.jpg', 'pessoas/faceolho.jpg', 'pessoas/pessoas1.jpg', 'pessoas/pessoas2.jpg', 'pessoas/pessoas3.jpg', 'pessoas/pessoas4.jpg']
    #fotos = ['pessoas/carro1.jpg', 'pessoas/carro2.jpg', 'pessoas/carro3.jpg']
    #fotos = ['pessoas/gato1.jpg', 'pessoas/gato2.jpg', 'pessoas/gato3.jpg']

    imagem = cv2.imread(random.choice(fotos))
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.1, minNeighbors=9, minSize=(30, 30))

    for (x, y, l, a) in facesDetectadas:
        imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

    cv2.imshow("Faces encontradas", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

janela = tk.Tk()
janela.title('Captura de Faces')
janela['bg'] = 'gray'
bt1 = tk.Button(janela, width=20, text='Webcam', command=webcam)
bt1.place(x=80, y=150)
bt2 = tk.Button(janela, width=20, text='Imagens', command=face)
bt2.place(x=80, y=180)
bt3 = tk.Button(janela, width=20, text = 'Sair', command=janela.destroy)
bt3.place(x=80, y=210)
janela.geometry('300x300+200+200')

img = tk.PhotoImage(file='pessoas/tst.png')
img1 = tk.Label(janela, imag = img)
img1.place(x=100, y=30)
#lb = tk.Label(janela, text='oi')
#lb.place(x=100, y=100)

janela.mainloop()

