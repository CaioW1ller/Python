class Proprietario:
    def __init__(self, nome, endereco, cpf, email, saldo_bancario):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.email = email
        self.saldo_bancario = saldo_bancario
        self.adimplente = saldo_bancario > 0
        self.veiculos = {}

    def ver_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")
        print(f"Saldo Bancário: R$ {self.saldo_bancario:.2f}")
        print(f"Adimplente: {'Sim' if self.adimplente else 'Não'}")
        print("Veículos:")
        if self.veiculos:
            for _, veiculo in self.veiculos.items():
                print(f"Modelo: {veiculo.modelo}, Placa: {veiculo.placa}, Ano: {veiculo.ano}, Eixos: {veiculo.eixos}")
        else:
            print("Nenhum veículo cadastrado.")

class Veiculo:
    def __init__(self, modelo, placa, ano, eixos):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.eixos = eixos

    def add_veiculo(self, proprietario):
        if self.placa not in proprietario.veiculos:
            proprietario.veiculos[self.placa] = self
            print(f'Veículo {self.modelo} com a placa {self.placa} adicionado com sucesso!')
        else:
            print('O veículo já está cadastrado!')

    def rem_veiculo(self, proprietario):
        if self.placa in proprietario.veiculos:
            del proprietario.veiculos[self.placa]
            print(f'O veículo {self.modelo} com a placa {self.placa} removido com sucesso!')
        else:
            print('Não existe tal veículo cadastrado!')

class Tag:
    def __init__(self, proprietario, veiculo):
        self.proprietario = proprietario
        self.veiculo = veiculo
        self.ativo = True

    def cancel(self):
        self.ativo = False
        print(f"Tag para o veículo {self.veiculo.placa} foi cancelada.")

class Pedagio:
    def __init__(self):
        self.tags = []

    def add_tag(self, proprietario, veiculo):
        tag = Tag(proprietario, veiculo)
        self.tags.append(tag)
        print(f"Tag registrada para o veículo {veiculo.modelo} com a placa {veiculo.placa}!")

    def rem_tag(self, veiculo):
        for tag in self.tags:
            if tag.veiculo == veiculo and tag.ativo:
                tag.cancel()
                return
        print("Tag não encontrada ou já cancelada!")

    def calculo_tarifa(self, eixos):
        tarifas = [2.40, 4.80, 7.20, 9.60, 12.00, 14.40]
        if 1 <= eixos <= len(tarifas):
            valor = tarifas[eixos - 1]
            print(f'Valor da tarifa é de R$ {valor:.2f}!')
            return valor
        else:
            print("Número de eixos inválido.")
            return 0

    def passagem_pedagio(self, placa):
        for tag in self.tags:
            if tag.veiculo.placa == placa:
                if tag.ativo and tag.proprietario.adimplente:
                    taxa = self.calculo_tarifa(tag.veiculo.eixos)
                    if tag.proprietario.saldo_bancario >= taxa:
                        tag.proprietario.saldo_bancario -= taxa
                        print(f'Foi debitado de sua conta bancária R$ {taxa:.2f}, saldo restante = R$ {tag.proprietario.saldo_bancario:.2f}!')
                    else:
                        print(f'Saldo insuficiente! Você possui apenas R$ {tag.proprietario.saldo_bancario:.2f}.')
                elif not tag.ativo:
                    print('O pagamento terá que ser feito manualmente, pois a Tag está desativada ou não existe!')
                elif not tag.proprietario.adimplente:
                    print('O pagamento terá que ser feito manualmente, pois você está inadimplente!')
                return
        print("Veículo não registrado para cobrança automática.")

proprietarios = {}
pedagio = Pedagio()

while True:
    escolha = input('\nMenu de Escolhas:\n1. Cadastrar Proprietário\n2. Adicionar Veículo\n3. Remover Veículo\n4. Ativar Tag\n5. Remover Tag\n6. Passagem no Pedágio\n7. Ver Dados do Proprietário\n8. Sair\nEscolha: ')
    
    if escolha == '1':
        nome = input('Insira seu nome: ')
        endereco = input('Insira seu endereço: ')
        cpf = input('Insira seu CPF: ')
        email = input('Insira seu e-mail: ')
        saldo_bancario = float(input('Insira seu saldo bancário: '))
        proprietario = Proprietario(nome, endereco, cpf, email, saldo_bancario)
        proprietarios[cpf] = proprietario
        print(f'Proprietário {nome} cadastrado com sucesso!')

    elif escolha == '2':
        cpf = input('Informe o CPF do proprietário: ')
        if cpf in proprietarios:
            modelo = input('Insira o modelo do veículo: ')
            placa = input('Insira a placa do veículo (com o -): ')
            ano = input('Insira o ano do veículo: ')
            eixos = int(input('Insira o número de eixos do veículo: '))
            veiculo = Veiculo(modelo, placa, ano, eixos)
            veiculo.add_veiculo(proprietarios[cpf])
        else:
            print('Proprietário não encontrado.')

    elif escolha == '3':
        cpf = input('Informe o CPF do proprietário: ')
        if cpf in proprietarios:
            placa = input('Insira a placa do veículo para removê-lo: ')
            if placa in proprietarios[cpf].veiculos:
                veiculo = proprietarios[cpf].veiculos[placa]
                veiculo.rem_veiculo(proprietarios[cpf])
            else:
                print('Veículo não encontrado.')
        else:
            print('Proprietário não encontrado.')

    elif escolha == '4':
        cpf = input('Informe o CPF do proprietário: ')
        if cpf in proprietarios:
            placa = input('Informe a placa do veículo para ativar a Tag: ')
            if placa in proprietarios[cpf].veiculos:
                veiculo = proprietarios[cpf].veiculos[placa]
                pedagio.add_tag(proprietarios[cpf], veiculo)
            else:
                print('Veículo não encontrado.')
        else:
            print('Proprietário não encontrado.')

    elif escolha == '5':
        cpf = input('Informe o CPF do proprietário: ')
        if cpf in proprietarios:
            placa = input('Informe a placa do veículo para remover a Tag: ')
            if placa in proprietarios[cpf].veiculos:
                veiculo = proprietarios[cpf].veiculos[placa]
                pedagio.rem_tag(veiculo)
            else:
                print('Veículo não encontrado.')
        else:
            print('Proprietário não encontrado.')

    elif escolha == '6':
        placa = input('Informe a placa do veículo para passar no pedágio: ')
        pedagio.passagem_pedagio(placa)

    elif escolha == '7':
        cpf = input('Informe o CPF do proprietário: ')
        if cpf in proprietarios:
            proprietarios[cpf].ver_dados()
        else:
            print('Proprietário não encontrado.')

    elif escolha == '8':
        break

    else:
        print('Opção inválida. Escolha novamente!')