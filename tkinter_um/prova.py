import tkinter as tk

def converter_cm_para_metros():
    cm = entry_cm.get()
    
    if cm.isdigit() or (cm.count('.') == 1 and cm.replace('.', '').isdigit()):
        cm = float(cm)
        metros = cm / 100.0
        resultado.config(text=f"{cm} centímetros são {metros} metros", fg="green")
    else:
        resultado.config(text="Por favor, insira um valor válido em centímetros.", fg="red")

root = tk.Tk()
root.title("Conversor de Centímetros para Metros")

label_cm = tk.Label(root, text="Centímetros:")
label_cm.pack()
entry_cm = tk.Entry(root)
entry_cm.pack()

converter_button = tk.Button(root, text="Converter", command=converter_cm_para_metros, bg="blue", fg="white")
converter_button.pack()

resultado = tk.Label(root, text="", fg="green")
resultado.pack()

root.mainloop()
