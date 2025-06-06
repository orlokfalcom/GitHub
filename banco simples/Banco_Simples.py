from datetime import datetime

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{data_hora} - Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Erro: Valor inválido! Tente novamente.")
    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    try:
        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f} por saque.")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Operação falhou! Você já realizou {LIMITE_SAQUES} saques hoje. Tente novamente amanhã.")
        else:
            saldo -= valor
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{data_hora} - Saque: R$ {valor:.2f}")
            numero_saques += 1
            print("Saque realizado com sucesso!")
    except ValueError:
        print("Erro: Valor inválido! Tente novamente.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato, saldo_inicial):
    print("\n================ EXTRATO ================")
    print(f"Saldo inicial: R$ {saldo_inicial:.2f}")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\n".join(extrato))
    print(f"Saldo final: R$ {saldo:.2f}")
    print("==========================================")


def main():
    saldo = 0
    saldo_inicial = saldo
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    
    while True:
        opcao = input(menu).lower()
        
        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato, saldo_inicial)
        elif opcao == "q":
            print("Obrigado por usar nosso banco! Até logo.")
            break
        else:
            print("Operação inválida! Tente novamente.")


if __name__ == "__main__":
    main()
