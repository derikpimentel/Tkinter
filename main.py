# Biblioteca para criação de janelas
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from pystray import MenuItem as item, Icon
from PIL import Image

class Application:
    def __init__(self, master=None):
        # Função para mostrar a janela quando o usuário clicar no ícone da bandeja
        def mostrar_janela(icon, item):
            icon.stop()  # Para o ícone da bandeja
            master.deiconify()  # Mostra a janela do Tkinter
            #master.lift()        # Traz a janela para a frente
            master.wm_attributes('-topmost', True)  # Coloca a janela como "sempre no topo"
            master.after(1000, lambda: master.wm_attributes('-topmost', False))  # Remove o "sempre no topo" após 1 segundo
            #master.focus_force()  # Garante que a janela receba o foco

        # Função para ocultar a janela e enviar para a bandeja do sistema
        def para_bandeja():
            master.withdraw()  # Oculta a janela do Tkinter
            self.icon.run()

        def sair(icon, item):
            icon.stop()
            master.quit()

        # Define o título da janela
        master.title("Olá mundo!")

        # Criar ícone para a bandeja (um ícone de exemplo usando PIL)
        self.image = Image.new('RGB', (64, 64), color=(73, 109, 137))

        # Crie o menu com pystray
        self.submenu = (item('Mostrar', mostrar_janela), item('Sair', sair))  # Usando o menu do pystray
        self.submenu = (mostrar_janela)

        # Criar e adicionar o ícone na bandeja
        self.icon = Icon("Tkinter App", self.image, menu=self.submenu)

        # Detectar evento de minimizar a janela
        master.bind("<Unmap>", lambda event: para_bandeja() if master.state() == 'iconic' else None)

        # Define o tamanho da janela (largura x altura)
        #master.geometry("500x500")

        # Desabilita a maximização
        master.resizable(False, False)

        self.font = ("Verdana", "8")

        # Cria o menu principal
        self.menu_bar = Menu(master)

        # Criando o menu "Arquivo"
        self.menu_file = Menu(self.menu_bar, tearoff=0)
        self.menu_file.add_command(label="Novo", command=self.new_file) # Adiciona a opção "Novo"
        self.menu_file.add_command(label="Abrir") # Adiciona a opção "Abrir"
        self.menu_file.add_separator() # Adiciona um separador
        self.menu_file.add_command(label="Sair", command=master.quit) # Adiciona a opção "Sair"

        # Adiciona o menu "Arquivo" à barra de menu
        self.menu_bar.add_cascade(label="Arquivo", menu=self.menu_file)

        # Criando outro menu, como "Editar"
        self.menu_edit = Menu(self.menu_bar, tearoff=0)
        self.menu_edit.add_command(label="Copiar")
        self.menu_edit.add_command(label="Colar")

        # Adiciona o menu "Editar" à barra de menu
        self.menu_bar.add_cascade(label="Editar", menu=self.menu_edit)

        # Configura a janela para usar essa barra de menu
        master.config(menu=self.menu_bar)

        # Adiciona um rótulo (label) à janela
        self.label = Label(master, text="Seja bem-vindo!")
        self.label.pack(pady=20)

        self.container01 = Frame(master)
        self.container01.pack(pady=20)

        # Criando a Treeview (Tabela)
        self.table = Treeview(self.container01, columns=("Nome", "Idade"), show="headings")
        self.table.heading("Nome", text="Nome")
        self.table.heading("Idade", text="Idade")
        self.table.column("Nome")
        self.table.column("Idade", width=100)

        # Adiciona uma barra de rolagem à tabela
        self.scrollbar = Scrollbar(self.container01, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')
        
        # Insere a tabela na janela
        self.table.pack()
        
        # Campos de entrada para adicionar novos dados
        self.container02 = Frame(master)
        self.container02.pack(pady=10)

        Label(self.container02, text="Nome:").grid(row=0, column=0, padx=5)
        self.txt_name = Entry(self.container02)
        self.txt_name.grid(row=0, column=1, padx=5)

        Label(self.container02, text="Idade:").grid(row=1, column=0, padx=5)
        self.txt_age = Entry(self.container02)
        self.txt_age.grid(row=1, column=1, padx=5)

        # Botões para adicionar e remover dados
        self.container03 = Frame(master)
        self.container03.pack(pady=10)

        self.btn_new = Button(self.container03, text="Adicionar")
        self.btn_new["command"] = self.new_row
        self.btn_new.grid(row=0, column=0, padx=10)

        self.btn_delete = Button(self.container03, text="Remover Selecionado")
        self.btn_delete["command"] = self.delete_row
        self.btn_delete.grid(row=0, column=1, padx=10)

        # Adiciona um botão à janela
        self.btn_click = Button(master, text="Clique aqui!")
        self.btn_click["command"] = lambda: print("Botão clicado!")
        self.btn_click.pack(pady=10)

    # Função para ações de menu
    def new_file(self):
        messagebox.showinfo("Novo Arquivo", "Você clicou em Novo Arquivo!")

    # Função para adicionar uma nova linha na tabela
    def new_row(self):
        name = self.txt_name.get()
        age = self.txt_age.get()
        if name and age:
            self.table.insert('', 'end', values=(name, age))
            self.txt_name.delete(0, END)
            self.txt_age.delete(0, END)

    # Função para remover a linha selecionada
    def delete_row(self):
        selected_item = self.table.selection()
        if selected_item:
            self.table.delete(selected_item)

root = Tk() # Criando a janela principal
Application(root)
root.mainloop() # Mantêm a janela aberta