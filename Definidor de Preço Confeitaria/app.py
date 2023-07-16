import tkinter as tk

# Define o preço de cada produto
produtos = {
    "Bolo de chocolate": 15.00,
    "Torta de frutas": 20.00,
    "Pão de mel": 5.00,
    "Brigadeiro": 3.00,
    "Beijinho": 2.00
}

# Armazena as informações dos clientes
clientes = {}

# Cria a janela principal
janela = tk.Tk()
janela.title("Registro de gastos de clientes")

# Cria as etiquetas para exibir as informações dos clientes
etiquetas = {}

def atualiza_etiquetas():
    for i, (nome, gasto) in enumerate(clientes.items()):
        if nome in etiquetas:
            etiquetas[nome]["nome"].config(text=nome)
            etiquetas[nome]["gasto"].config(text=f"R$ {gasto:.2f}")
            etiquetas[nome]["media"].config(text=f"R$ {gasto / len(clientes):.2f}")
        else:
            etiquetas[nome] = {
                "nome": tk.Label(janela, text=nome),
                "gasto": tk.Label(janela, text=f"R$ {gasto:.2f}"),
                "media": tk.Label(janela, text=f"R$ {gasto / len(clientes):.2f}")
            }
            etiquetas[nome]["nome"].grid(row=i + 1, column=0)
            etiquetas[nome]["gasto"].grid(row=i + 1, column=1)
            etiquetas[nome]["media"].grid(row=i + 1, column=2)

# Cria a função para adicionar um novo cliente
def adiciona_cliente():
    # Pega o nome do cliente
    nome = input_nome.get()
    input_nome.delete(0, tk.END)

    # Pega o preço do produto
    preco = float(input_preco.get())
    input_preco.delete(0, tk.END)

    # Adiciona o gasto do cliente ao dicionário de clientes
    if nome in clientes:
        clientes[nome] += preco
    else:
        clientes[nome] = preco

    # Atualiza as etiquetas
    atualiza_etiquetas()

# Cria o label e o campo de entrada para o nome do cliente
label_nome = tk
