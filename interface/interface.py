import tkinter as tk
from tkinter.ttk import Combobox
import os
import sys
sys.path.insert(0, './')
from artigo import Artigo

def nomesArquivos() -> list:
    dir_path = 'artigos'

    files = os.listdir(dir_path)
    files = [str(i +1) + '. ' + file for i, file in enumerate(files)]

    return files

def mostrarDadoExtraido(rotulo: str, texto : str):
    janelaMostrarDadosExtraidos = tk.Toplevel(root)
    janelaMostrarDadosExtraidos.title(rotulo)

    text = tk.Text(janelaMostrarDadosExtraidos)
    text.insert(tk.END, texto)
    text.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar = tk.Scrollbar(janelaMostrarDadosExtraidos)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)

    # Adiciona um botão para voltar
    back_button = tk.Button(janelaMostrarDadosExtraidos, text="Voltar", command=janelaMostrarDadosExtraidos.destroy)
    back_button.pack()

   


def telaExtracaoArtigo(arquivo: str):
    # Cria uma nova janela
    arquivo = arquivo.split('. ')[1]
    
    new_window = tk.Toplevel(root)
    new_window.title("Segunda Janela")

    label = tk.Label(new_window, text='Escolha o que você deseja visualizar do arquivo ' + arquivo)
    label.grid(row=0, column=0, columnspan=2) 

    artigoEscolhido = Artigo('artigos/CLASSIFICAÇÃO DE VEÍCULOS BASEADA EM DEEP LEARNING PARA APLICAÇÃO EM SEMÁFOROS INTELIGENTES LAVRAS – MG 2021.pdf')
    
    # Adiciona botões na nova janela
    button1 = tk.Button(new_window, text="1. Objetivo", command=lambda: mostrarDadoExtraido('Objetivo', artigoEscolhido.getObjetivo()))
    button1.grid(row=1, column=0)

    
    button2 = tk.Button(new_window, text="2. Problema", command=lambda: mostrarDadoExtraido('Problema', artigoEscolhido.getProblema()))
    button2.grid(row=1, column=1)
    
    button3 = tk.Button(new_window, text="3. Método ou metodologia", command=lambda: mostrarDadoExtraido('Método ou metodologia', artigoEscolhido.getMetodologia()))
    button3.grid(row=2, column=0)
    
    button4 = tk.Button(new_window, text="4. Contribuição", command=lambda: mostrarDadoExtraido('Contribuição', artigoEscolhido.getContribuicao()))
    button4.grid(row=2, column=1)
    
    button5 = tk.Button(new_window, text="5. Referência", command=lambda: mostrarDadoExtraido('Referência', artigoEscolhido.getReferencia()))
    button5.grid(row=3, column=0)

    button6 = tk.Button(new_window, text="Salvar dados", command=lambda: artigoEscolhido.salvarArtigo())
    button6.grid(row=3, column=1)
    
    # Adiciona um botão para voltar
    back_button = tk.Button(new_window, text="Voltar", command=new_window.destroy)
    back_button.grid(row=4, column=0, columnspan=2)  

root = tk.Tk()
root.title("Exemplo de Interface Gráfica")

texto = '''Trabalho de inteligência artificial
O objetivo desse trabalho é utilizar técnicas de PLN para analisar textos científicos

equipe: 
    Álvaro de Araújo
    Karoline Romero
    Rafael Torres
'''

# Texto explicativo
label = tk.Label(root, text=texto)
label.pack()

# Botão combobox
combobox = Combobox(root, values=nomesArquivos())
combobox.pack()

button = tk.Button(root, text="extrair dados", command=lambda: telaExtracaoArtigo(combobox.get()))
button.pack()

button = tk.Button(root, text="Sair", command=root.destroy)
button.pack()

root.mainloop()