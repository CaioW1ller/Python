agenda_telefonica = {}  # Agenda telefonica inicialmente vazia

def incluir_contato(nome, *telefones):  # Função que recebe um nome e infinitos telefones
    if nome not in agenda_telefonica:  # Condição para verificar se o nome não está na agenda
        agenda_telefonica[nome] = list(telefones)  # Adiciona o nome com os telefones na agenda
        print("Nome adicionado a agenda telefonica!")  # Mensagem de confirmação
    else:
        agenda_telefonica[nome].extend(telefones)  # Adiciona os novos telefones ao contato existente
        print("Telefone(s) incluidos para o nome correspondente!")

def incluir_telefone(nome, numero):  # Função que adiciona um telefone a um contato existente
    if nome in agenda_telefonica:  # Verifica se o nome está na agenda
        agenda_telefonica[nome].append(numero)  # Adiciona o novo número ao contato
        print("Número adicionado com sucesso para o contato existente.") 
    else:
        print("O contato não existe na agenda.")

def excluir_nome(nome):  # Função que exclui um contato da agenda
    if nome in agenda_telefonica:  # Verifica se o nome está na agenda
        del agenda_telefonica[nome]  # Remove o contato da agenda
        print("Nome excluido com sucesso!")  
    else:
        print("O nome não existe na agenda.") 

def excluir_telefone(nome, telefone):  # Função que exclui um telefone de um contato existente
    if nome in agenda_telefonica:  # Verifica se o nome está na agenda
        if telefone in agenda_telefonica[nome]:  # Verifica se o telefone está associado ao nome
            agenda_telefonica[nome].remove(telefone)  # Remove o telefone do contato
            print("Número removido com sucesso do contato existente.")  
        else:
            print("O número de telefone não está associado a este nome.") 
    else: 
        print("O nome não existe na lista telefonica.")

def consultar_telefone():  # Função que exibe todos os contatos e seus telefones
    if agenda_telefonica:  # Verifica se há contatos na agenda
        print("Lista Telefonica: ")  # Título da lista
        for nome, telefones in agenda_telefonica.items():  # Itera sobre os contatos e seus telefones
            telefones_f = ", ".join(telefones)  # Junta os telefones em uma string separada por vírgulas
            print(f"{nome}: {telefones_f}")  # Exibe o nome e os telefones formatados
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

    if escolha == '1':  # Se a escolha for 1
        nome = input("Digite o nome do contato: ")  # Solicita o nome do contato
        telefones = input("Digite os números de telefone separados por espaço: ").split(' ')  # Solicita os telefones e os separa por espaço
        incluir_contato(nome, *telefones)  # Chama a função para incluir o contato com os telefones
    elif escolha == '2':  # Se a escolha for 2
        nome = input("Digite o nome do contato: ")  # Solicita o nome do contato
        numero = input("Digite o número a ser adicionado: ")  # Solicita o número a ser adicionado
        incluir_telefone(nome, numero)  # Chama a função para incluir o telefone no contato
    elif escolha == '3':  # Se a escolha for 3
        nome = input("Digite o nome do contato a ser excluído: ")  # Solicita o nome do contato a ser excluído
        excluir_nome(nome)  # Chama a função para excluir o contato
    elif escolha == '4':  # Se a escolha for 4
        nome = input("Digite o nome do contato: ")  # Solicita o nome do contato
        telefone = input("Digite o telefone a ser removido: ")  # Solicita o telefone a ser removido
        excluir_telefone(nome, telefone)  # Chama a função para excluir o telefone do contato
    elif escolha == '5':  # Se a escolha for 5
        consultar_telefone()  # Chama a função para consultar os contatos e telefones
    elif escolha == '6':  # Se a escolha for 6
        break  # Encerra o loop e termina o programa
