import tkinter as tk

def verificar_login():
    email = entry_email.get()
    senha = entry_senha.get()

    if "@" in email and len(senha) > 6:
        resultado.config(text="Login bem-sucedido!", fg="green")
    else:
        resultado.config(text="Erro: Verifique o e-mail e senha.", fg="red")

root = tk.Tk()
root.title("Tela de Login")

label_email = tk.Label(root, text="E-mail:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_senha = tk.Label(root, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(root, show="*")
entry_senha.pack()

verificar_button = tk.Button(root, text="Login", command=verificar_login, bg="blue", fg="white")
verificar_button.pack()

resultado = tk.Label(root, text="")
resultado.pack()

root.mainloop()