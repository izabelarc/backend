from tkinter import *

janela = Tk()
#widgets

#labels
titulo = Label(text = "INFINITY SCHOOL",
               fg="black",
               bg="orange")
nome_label = Label(text="Insira seu nome")

#entrys
entrada=Entry()

#definindo localização
titulo.pack()
nome_label.pack()
entrada.pack()

janela.mainloop()