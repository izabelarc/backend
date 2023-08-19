from tkinter import ttk

#Substituindo as ferramentas nativas do Tkinter por
#ferramentas melhores, mais modernas
from tkinter import *
from tkinter.ttk import *

#criando a janela
janela = Tk()
janela.title("Combobox dias da semana")

dias_semana = [
    "Domingo",
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sabado"
]

combobox = ttk.Combobox(janela, values =dias_semana)
#renderiza
combobox.pack(padx=75, pady=20)

#Rodando a janela
janela.mainloop()