import os
from typing import List, Dict, Union, Tuple

def menu() -> str:
    menu_options: str = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuario
    [q] Sair

    => """
    return input(menu_options).lower()

def depositar(saldo: float, valor_deposito: float, extrato: str) -> Tuple[float, str]:
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Você Depositou {valor_deposito:.2f} em sua conta")
    else:
        print("Operação falhou! O valor informado é inválido.")
    print("=" * 39)

    return saldo, extrato

def sacar(saldo: float, valor_saque: float, extrato: str, limite: float, 
          numero_saques: int, limite_saques: int) -> Tuple[float, str]:
    excedeu_saldo: bool = valor_saque > saldo
    excedeu_limite: bool = valor_saque > limite
    excedeu_saques: bool = numero_saques >= limite_saques

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

    return saldo, extrato

def exibir_extrato(saldo: float, extrato: str) -> None:
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=" * 39)

def criar_usuario(usuarios: List[Dict]) -> None:
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ").title()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").title()

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def listar_usuarios(usuarios: List[Dict]) -> None:
    for usuario in usuarios:
        linha = f"""\
            Nome:\t{usuario['nome']}
            CPF:\t{usuario['cpf']}
            Data de Nascimento:\t{usuario['data_nascimento']}
            Endereço:\t{usuario['endereco']}
        """
        print(linha)

def filtrar_usuario(cpf: str, usuarios: List[Dict]) -> Dict[str, int]:
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia: str, numero_conta: int, usuarios: List[Dict]) -> Union[None, Dict[str, int]]:
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas: List[Dict]) -> None:
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(linha)

def main() -> None:
    AGENCIA = "0001"
    LIMITE_SAQUES: int = 3

    saldo: float = 0.0
    limite: float = 500.0
    extrato: str = ""
    numero_saques: int = 0
    usuarios: List[Dict] = []
    contas: List[Dict] = []

    while True:
        opcao: str = menu()

        match opcao:
            case "d":
                os.system('cls')
                print("\n================ DEPÓSITO ================\n")
                valor_deposito: float = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor_deposito, extrato)


            case "s":
                os.system('cls')
                print("\n================ SAQUE ================\n")
                valor_saque: float = float(input("Informe o valor do saque: "))
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor_saque=valor_saque,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )

            case "e":
                os.system('cls')
                print("\n================ EXTRATO ================\n")
                exibir_extrato(saldo, extrato=extrato)

            case "nu":
                os.system('cls')
                print("\n================ CRIAR USUARIO ================\n")
                criar_usuario(usuarios)
            
            case "nc":
                os.system('cls')
                print("\n================ CRIAR CONTA ================\n")
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)
            
            case "lc":
                os.system('cls')
                print("\n================ TODAS AS CONTAS ================\n")
                listar_contas(contas)

            case "lu":
                os.system('cls')
                print("\n================ TODOS OS USUÁRIOS ================\n")
                listar_usuarios(usuarios)  

            case "q":
                print("Você saiu! Até a próxima.")
                break

            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
