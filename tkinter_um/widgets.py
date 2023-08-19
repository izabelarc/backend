'''Alguns exemplos de widgets:
● labels(Label): Usado para exibir texto na tela.
● caixas de texto(Entry): Widget de entrada de dados que permite apenas uma única linha
de texto.
● botões(Button): Um botão que pode conter texto e realizar uma ação quando clicado.
● frames(Frame): Uma região usada para agrupar widgets relacionados ou fornecer
preenchimento entre widgets.
● checkbox(Checkbutton): Uma caixa de seleção para implementar ações do tipo
liga/desliga.
● radiobutton(Radiobutton): Uma caixa de seleção para implementar uma de muitas
seleções.
● combobox(Combobox): Usado para exibir uma lista de opções disponíveis.'''

'''Adicionamos o widget Label a janela,
mas para ele aparecer precisamos
informar ao Tkinter para renderizar este
widget.
Existem diversos métodos de
renderização de widgets em uma
janela Tkinter.
Neste código usamos o método .pack()

obs: Breve falaremos sobre pack(),
grid() e place() nas próximas seções.'''

'''Definindo cores (Label)
Podemos informar cor para o texto o fundo da nossa label através dos seguintes
argumentos.
● foreground ou fg: cor de texto
● background ou bg: cor do fundo'''

'''ENTRY- A classe Entry do Tkinter é usada para criar uma
caixa de texto na qual o usuário pode inserir textos.
É um dos elementos de controle mais comuns e
úteis para receber entrada de dados do usuário
em uma GUI.'''


'''BUTTON- A classe Button do Tkinter é usada para criar
botões em uma interface gráfica. Botões são
elementos de controle interativos que executam
ações quando clicados pelo usuário.

Para criar um botão usando a classe Button(),
você precisa fornecer o objeto pai(geralmente a
janela principal) como primeiro argumento e pode
definir o texto exibido no botão usando o
argumento text.
● .get() : obter o texto inserido

● .delete() : apaga o texto inserido

● .insert() : inserir o texto'''

'''COMMAND- Podemos associar uma função ou um método
específico para ser executado quando o botão for
clicado. isso é feito usando o argumento
command e passando a função ou o método
desejado.'''