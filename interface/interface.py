import tkinter as tk
from tkinter.ttk import Combobox
# from artigo import Artigo
import os

def nomesArquivos() -> list:
    dir_path = 'ArquivosFuncionando'

    files = os.listdir(dir_path)
    files = [str(i +1) + '. ' + file for i, file in enumerate(files)]

    return files

def on_button_click(arquivo: str):
    # Cria uma nova janela
    arquivo = arquivo.split('. ')[1]
    new_window = tk.Toplevel(root)
    new_window.title("Segunda Janela")

    label = tk.Label(new_window, text='Escolha o que você deseja visualizar do arquivo ' + arquivo)
    label.pack()    
    
    # Adiciona um botão combobox na nova janela
    combobox = Combobox(new_window, values=["1. Objetivo", 
                                            "2. Problema", 
                                            "3. Método ou metodologia",
                                            "4. Contribuição", 
                                            "5. Referência"])
    combobox.pack()
    
    # Adiciona dois botões na nova janela
    button1 = tk.Button(new_window, text="Botão 1")
    button1.pack()
    
    button2 = tk.Button(new_window, text="Voltar")
    button2.pack()


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

button = tk.Button(root, text="extrair dados", command=lambda: on_button_click(combobox.get()))
button.pack()

root.mainloop()