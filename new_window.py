from tkinter import Toplevel, Text, END

class NewWindow:
    def __init__(self, master):        
        # Cria uma nova janela
        self.top_master = Toplevel(master)
        self.top_master.title("Nova Janela")

        # Cria um widget Text para mostrar o texto
        self.text_widget = Text(self.top_master, height=10, width=20, wrap='word', bd=0, bg=self.top_master.cget('bg'), font=("Calibri", 10))
        self.text_widget.pack(padx=20, pady=20)

        # Adiciona um texto inicial
        self.text_widget.insert(END, "Este é um texto que pode ser selecionado e copiado.")

        # Desabilita a edição do texto
        self.text_widget.config(state='disabled')