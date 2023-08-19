from tkinter import *

janela = Tk()
#widgets

#labels
titulo = Label(text = "INFINITY SCHOOL",
               fg="black",
               bg="orange")
nome_label = Label(text="Insira seu nome")

#entrys
entrada=Entry(fg="#2a2a2a",
              bg="#f3e8e8",
              width=30)

#botões
enviar = Button(janela, text="submit")

#definindo localização
titulo.pack()
nome_label.pack()
entrada.pack()
enviar.pack()

janela.mainloop()