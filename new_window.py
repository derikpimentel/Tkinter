import os
import json
from tkinter import *

class NewWindow:
    def __init__(self, master=None):        
        # Cria uma nova janela
        self.master = Toplevel(master)
        self.master.title("Nova Janela")

        # Cria um widget Text para mostrar o texto
        self.text_widget = Text(self.master, height=20, width=30, wrap='word', bd=0, bg=self.master.cget('bg'), font=("Calibri", 10))
        self.text_widget.pack(padx=10, pady=10)

        self.txt = """
    Primeiro teste
        Testando a formatação e o salvamento de arquivos de texto,
        para poder salvar em muitos formatos.
    Segundo teste
        Esse texto pode ser selecionado e copiado."""

        self.json = {
            "text": """
    Primeiro teste
        Testando a formatação e o salvamento de arquivos de texto,
        para poder salvar em muitos formatos.
    Segundo teste
        Esse texto pode ser selecionado e copiado."""
        }

        # Adiciona um texto inicial
        self.text_widget.insert(END, self.txt)

        # Desabilita a edição do texto
        self.text_widget.config(state='disabled')

        self.btn_save_txt = Button(self.master, text="Salvar TXT")
        self.btn_save_txt["command"] = self.save_to_txt
        self.btn_save_txt.pack(pady=10)

        self.btn_save_json = Button(self.master, text="Salvar JSON")
        self.btn_save_json["command"] = self.save_to_json
        self.btn_save_json.pack(pady=10)

        self.btn_open_json = Button(self.master, text="Abrir JSON")
        self.btn_open_json["command"] = self.load_to_json
        self.btn_open_json.pack(pady=10)

    def save_to_txt(self):
        # Abre (ou cria) o arquivo no modo de escrita e salva os dados
        with open("test.txt", "w") as archive:
            archive.write(self.txt)

    def save_to_json(self):
        # Salvando os dados como arquivo JSON
        with open("test.json", "w") as archive_json:
            json.dump(self.json, archive_json, indent=4)

    def load_to_json(self):
        # Carrega as configurações do arquivo JSON
        if os.path.exists("test.json"):
            with open("test.json", "r") as file:
                file_json = json.load(file) # Carrega o arquivo
                self.text_widget.config(state='normal') # Habilita a edição do texto
                self.text_widget.delete('1.0', END) # Apaga o texto existente
                self.text_widget.insert(END, file_json["text"]) # Insere o novo texto
                self.text_widget.config(state='disabled') # Desabilita a edição do texto