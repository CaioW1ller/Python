agenda_telefonica = {}

def incluir_contato(nome, *telefones):
    if nome not in agenda_telefonica:
        agenda_telefonica[nome] = list(telefones)
        print("Nome adicionado a agenda telefonica!")
    else:
        agenda_telefonica[nome].extend(telefones)
        print("Telefone(s) incluidos para o nome correspondente!")

def incluir_telefone(nome, numero):
    if nome in agenda_telefonica:
        agenda_telefonica[nome].append(numero)
        print("Número adicionado com sucesso para o contato existente.")
    else:
        print("O contato não existe na agenda.")

def excluir_nome(nome):
    if nome in agenda_telefonica:
        del agenda_telefonica[nome]
        print("Nome excluido com sucesso!")
    else:
        print("O nome não existe na agenda.")

def excluir_telefone(nome, telefone):
    if nome in agenda_telefonica:
        if telefone in agenda_telefonica[nome]:
            agenda_telefonica[nome].remove(telefone)
            print("Número removido com sucesso do contato existente.")
        else:
            print("O número de telefone não está associado a este nome.")
    else:
        print("O nome não existe na lista telefonica.")

def consultar_telefone():
    if agenda_telefonica:
        print("Lista Telefonica:")
        for nome, telefones in agenda_telefonica.items():
            telefones_f = ", ".join(telefones)
            print(f"{nome}: {telefones_f}")
    else:
        print("A lista telefonica está vazia.")

def menu():
    print('AGENDA TELEFONICA\n')
    print('1. Criar Contato')
    print('2. Incluir Telefone')
    print('3. Excluir Nome')
    print('4. Excluir Telefone')
    print('5. Consultar Telefone')
    print('6. Sair\n')
    
    opcao = input('Escolha uma opção: ')
    return opcao

while True:
    escolha = menu()

    if escolha == '1':
        nome = input("Digite o nome do contato: ")
        telefones = input("Digite os números de telefone separados por espaço: ").split(' ')
        incluir_contato(nome, *telefones)
    elif escolha == '2':
        nome = input("Digite o nome do contato: ")
        numero = input("Digite o número a ser adicionado: ")
        incluir_telefone(nome, numero)
    elif escolha == '3':
        nome = input("Digite o nome do contato a ser excluído: ")
        excluir_nome(nome)
    elif escolha == '4':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone a ser removido: ")
        excluir_telefone(nome, telefone)
    elif escolha == '5':
        consultar_telefone()
    elif escolha == '6':
        break
