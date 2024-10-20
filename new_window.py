from tkinter import Toplevel, Label, Button

class NewWindow:
    def __init__(self, master):
        self.master = master
        
        # Cria uma nova janela
        self.nova_janela = Toplevel(self.master)
        self.nova_janela.title("Nova Janela")

        # Adiciona um rótulo à nova janela
        label = Label(self.nova_janela, text="Esta é uma nova janela!")
        label.pack(pady=20)