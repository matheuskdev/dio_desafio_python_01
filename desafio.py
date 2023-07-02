import os
print("Bem-vindo(a) ao DioBank")

menu: str = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo: float = 0.0
limite: float = 500.0
extrato: str = ""
numero_saques: int = 0
LIMITE_SAQUES: int = 3

while True:
    opcao: str = input(menu).lower()

    match opcao:
        case "d":
            os.system('cls')
            print("\n================ DEPÓSITO ================\n")
            valor_deposito: float = float(input("Informe o valor do depósito: "))

            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                print(f"Você Depósitou {valor_deposito:.2f} em sua conta")
            else:
                print("Operação falhou! O valor informado é inválido.")
            print("=" * 39)


        case "s":
            os.system('cls')
            print("\n================ SAQUE ================\n")
            valor_saque: float = float(input("Informe o valor do saque: "))

            excedeu_saldo: bool = valor_saque > saldo
            excedeu_limite: bool = valor_saque > limite
            excedeu_saques: bool = numero_saques >= LIMITE_SAQUES

            match (excedeu_saldo, excedeu_limite, excedeu_saques):
                case (True, _, _):
                    print("Operação falhou! Você não tem saldo suficiente.")
                case (_, True, _):
                    print("Operação falhou! O valor do saque excede o limite.")
                case (_, _, True):
                    print("Operação falhou! Número máximo de saques excedido.")
                case (_, _, _):
                    if valor_saque > 0:
                        saldo -= valor_saque
                        extrato += f"Saque: R$ {valor_saque:.2f}\n"
                        numero_saques += 1
                        print(f"Você Sacou: R$ {valor_saque}")
                    else:
                        print("Operação falhou! O valor informado é inválido.")
            print("=" * 39)

        case "e":
            os.system('cls')
            print("\n================ EXTRATO ================\n")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=" * 39)

        case "q":
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
