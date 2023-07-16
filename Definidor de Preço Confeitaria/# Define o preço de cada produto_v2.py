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

# Loop para registrar os gastos dos clientes
while True:
    # Pega o nome do cliente
    nome = input("Digite o nome do cliente (ou 'sair' para encerrar): ")
    if nome == "sair":
        break

    # Inicializa o gasto total do cliente
    gasto_total = 0

    # Loop para registrar os produtos comprados pelo cliente
    while True:
        # Exibe a lista de produtos disponíveis
        print("Produtos disponíveis:")
        for i, produto in enumerate(produtos.keys()):
            print(f"{i + 1}. {produto} - R$ {produtos[produto]}")

        # Pega o produto escolhido pelo cliente
        escolha = input("Escolha um produto (ou 'sair' para encerrar): ")
        if escolha == "sair":
            break
        else:
            escolha = int(escolha)

        # Adiciona o preço do produto ao gasto total do cliente
        gasto_total += produtos[list(produtos.keys())[escolha - 1]]

    # Adiciona o gasto total do cliente ao dicionário de clientes
    clientes[nome] = gasto_total

# Exibe o gasto total de cada cliente e sua média
gasto_total_geral = 0
for nome, gasto in clientes.items():
    gasto_total_geral += gasto
    print(f"{nome}: R$ {gasto}, média: R$ {gasto / len(clientes)}")
print(f"Gasto total geral: R$ {gasto_total_geral}")
