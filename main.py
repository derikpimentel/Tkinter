import tkinter as tk # Biblioteca para criação de janelas
from tkinter import ttk
from tkinter import messagebox

# Função para ações de menu
def new_file():
    messagebox.showinfo("Novo Arquivo", "Você clicou em Novo Arquivo!")

def exit():
    root.quit()

# Função para adicionar uma nova linha na tabela
def new_row():
    name = txt_name.get()
    age = txt_age.get()
    if name and age:
        tree.insert('', 'end', values=(name, age))
        txt_name.delete(0, tk.END)
        txt_age.delete(0, tk.END)

# Função para remover a linha selecionada
def delete_row():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

# Criando a janela principal
root = tk.Tk()

# Define o título da janela
root.title("Olá mundo!")

# Define o tamanho da janela (largura x altura)
root.geometry("500x500")

# Desabilita a maximização
root.resizable(False, False)

# Cria o menu principal
menu_bar = tk.Menu(root)

# Criando o menu "Arquivo"
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Novo", command=new_file)  # Adiciona a opção "Novo"
menu_file.add_command(label="Abrir")  # Adiciona a opção "Abrir"
menu_file.add_separator()  # Adiciona um separador
menu_file.add_command(label="Sair", command=exit)  # Adiciona a opção "Sair"

# Adiciona o menu "Arquivo" à barra de menu
menu_bar.add_cascade(label="Arquivo", menu=menu_file)

# Criando outro menu, como "Editar"
menu_edit = tk.Menu(menu_bar, tearoff=0)
menu_edit.add_command(label="Copiar")
menu_edit.add_command(label="Colar")

# Adiciona o menu "Editar" à barra de menu
menu_bar.add_cascade(label="Editar", menu=menu_edit)

# Configura a janela para usar essa barra de menu
root.config(menu=menu_bar)

# Adiciona um rótulo (label) à janela
label = tk.Label(root, text="Seja bem-vindo!")
label.pack(pady=20)

# Criando a Treeview (Tabela)
tree = ttk.Treeview(root, columns=("Nome", "Idade"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.column("Nome", width=200)
tree.column("Idade", width=100)

# Insere a tabela na janela
tree.pack(pady=20)

# Adiciona uma barra de rolagem à tabela
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Campos de entrada para adicionar novos dados
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Nome:").grid(row=0, column=0, padx=5)
txt_name = tk.Entry(frame)
txt_name.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Idade:").grid(row=1, column=0, padx=5)
txt_age = tk.Entry(frame)
txt_age.grid(row=1, column=1, padx=5)

# Botões para adicionar e remover dados
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

btn_new = tk.Button(frame_btn, text="Adicionar", command=new_row)
btn_new.grid(row=0, column=0, padx=10)

btn_delete = tk.Button(frame_btn, text="Remover Selecionado", command=delete_row)
btn_delete.grid(row=0, column=1, padx=10)

# Adiciona um botão à janela
button = tk.Button(root, text="Clique aqui!", command=lambda: print("Botão clicado!"))
button.pack(pady=10)

# Mantêm a janela aberta
root.mainloop()