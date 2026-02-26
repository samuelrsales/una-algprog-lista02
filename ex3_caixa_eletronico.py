"""
EXERCICIO:

Escreva o algoritmo para um saque: 
- Ler o valor_saque. 
- Verificar se o valor_saque é menor ou igual ao saldo_disponivel. 
- Se for, subtrair do saldo e entregar as notas. 
- Se não for, exibir "Saldo Insuficiente".
"""

db_contas = [
    {"id": 101, "saldo": 1500.50},
    {"id": 102, "saldo": 2300.00},
    {"id": 103, "saldo": 450.75},
    {"id": 104, "saldo": 10200.10},
    {"id": 105, "saldo": 85.00}
]


def sacar_dinheiro(database: list):
    
    print("Seja bem-vindo ao caixa eletrônico do Samuel!")
    print("-" * 20)
    print()

    id_conta = int(input("Digite o ID da sua conta: "))


    for i in database:
        if i["id"] == id_conta:
            print()
            print("CONTA ENCONTRADA.")
            print(f"SALDO DISPONÍVEL: R$ {i['saldo']}")
            print("_" * 20)
            print()

            valor_saque = float(input("Digite o valor do saque: "))

            if valor_saque < i["saldo"]:
                print("Saque realizado")
                i["saldo"] -= valor_saque
                print(f"Saldo atual: {i["saldo"]}")
                break

            else:
                print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")




sacar_dinheiro(db_contas)
