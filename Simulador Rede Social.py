class Usuario:
    loggins = {}

    def __init__(self, nome, email, data_nascimento, loggin):
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento
        self.loggin = loggin
        self.followers = []
        self.seguidos = []  
        self.mensagens = []

    def cadastrar(self):
        if self.loggin not in Usuario.loggins:
            Usuario.loggins[self.loggin] = self
            print(f'Usuário {self.loggin} cadastrado com sucesso!')

    def excluir_cadastro(self):
        if self.loggin in Usuario.loggins:
            del Usuario.loggins[self.loggin]
            print(f'Cadastro como loggin:{self.loggin} excluído com sucesso!')

    @staticmethod
    def listar_usuarios():
        for loggin, user in Usuario.loggins.items():
            print(f"Loggin: {loggin}, Nome: {user.nome}")

    def search(self):
        print(f"Nome: {self.nome}, Email: {self.email}, Data de Nascimento: {self.data_nascimento}, Loggin: {self.loggin}")

    def modificar_dados(self, novo_nome, novo_email):
        self.nome = novo_nome
        self.email = novo_email

    def follow(self, segundo_usuario_loggin):
        if segundo_usuario_loggin in Usuario.loggins:
            outro_usuario = Usuario.loggins[segundo_usuario_loggin]
            if self.loggin not in outro_usuario.followers:
                outro_usuario.followers.append(self.loggin)
                self.seguidos.append(segundo_usuario_loggin)
                print(f"{self.nome} agora está seguindo {outro_usuario.nome}")

    def unfollow(self, segundo_usuario_loggin):
        if segundo_usuario_loggin in Usuario.loggins:
            outro_usuario = Usuario.loggins[segundo_usuario_loggin]
            if self.loggin in outro_usuario.followers:
                outro_usuario.followers.remove(self.loggin)
                self.seguidos.remove(segundo_usuario_loggin)
                print(f"{self.nome} parou de seguir {outro_usuario.nome}")

    def list_followers(self):
        print(f"Seguidores de {self.nome}:")
        for seguidor in self.followers:
            seguidor = Usuario.loggins[seguidor]
            print(f"- {seguidor.nome}")

    def list_following(self):
        if self.seguidos:
            print(f"Usuários que {self.nome} está seguindo:")
            for seguido_loggin in self.seguidos:
                seguido = Usuario.loggins[seguido_loggin]
                print(f"- Loggin: {seguido.loggin}, Nome: {seguido.nome}")
        else:
            print(f"{self.nome} não está seguindo ninguém.")

    @staticmethod
    def usuario_com_mais_seguidores():
        if Usuario.loggins:
            maior_usuario = None
            max_seguidores = -1
        
            for loggin, user in Usuario.loggins.items():
                if len(user.followers) > max_seguidores:
                    max_seguidores = len(user.followers)
                    maior_usuario = user
        
            if maior_usuario:
                print(f"Usuário com mais seguidores:")
                print(f"Loggin: {maior_usuario.loggin}")
                print(f"Nome: {maior_usuario.nome}")
                print(f"Quantidade de seguidores: {len(maior_usuario.followers)}")
            else:
                print("Nenhum usuário possui seguidores.")
        else:
            print("Nenhum usuário cadastrado na rede.")
    
class Mensagem:
    def __init__(self, usuario):
        self.usuario = usuario

    def new_mensage(self, conteudo):
        mensagem = {'Conteudo': conteudo, 'comentarios': []}
        self.usuario.mensagens.append(mensagem)
        print(f"Mensagem adicionada ao usuário {self.usuario.nome}: {conteudo}")

    def new_coment_mensage(self, indice, coment, autor_loggin):
        if 0 <= indice < len(self.usuario.mensagens):
            autor = Usuario.loggins.get(autor_loggin)
            if autor:
                comentario = {'autor': autor.nome, 'conteudo': coment}
                self.usuario.mensagens[indice]['comentarios'].append(comentario)
                print(f"Comentário adicionado à mensagem {indice + 1} por {autor.nome}: {coment}")
            else:
                print(f"Usuário com loggin {autor_loggin} não encontrado.")
        else:
            print(f"Mensagem {indice + 1} não encontrada.")
    
    @staticmethod
    def exibir_mensagens_usuario_e_seguidos(usuario_loggin):
        if usuario_loggin in Usuario.loggins:
            usuario = Usuario.loggins[usuario_loggin]
        
            print(f"Mensagens de {usuario.nome}:")
            for i, mensagem in enumerate(usuario.mensagens):
                print(f"{i+1}. {mensagem['Conteudo']}")
        
            if usuario.seguidos:
                for seguido_loggin in usuario.seguidos:
                    seguido = Usuario.loggins[seguido_loggin]
                    print(f"\nMensagens de {seguido.nome}:")
                    for j, mensagem in enumerate(seguido.mensagens):
                        print(f"{j+1}. {mensagem['Conteudo']}")
            else:
                print(f"{usuario.nome} não segue ninguém.")
        else:
            print(f"Usuário com loggin {usuario_loggin} não encontrado.")

    @staticmethod
    def exibir_comentarios_mensagem(usuario_loggin, indice_mensagem):
        if usuario_loggin in Usuario.loggins:
            usuario = Usuario.loggins[usuario_loggin]
    
            if 0 <= indice_mensagem < len(usuario.mensagens):
                mensagem = usuario.mensagens[indice_mensagem]
                print(f"Comentários para a mensagem: {mensagem['Conteudo']}")
                if mensagem['comentarios']:
                    for comentario in mensagem['comentarios']:
                        print(f"- {comentario['autor']}: {comentario['conteudo']}")
                else:
                    print("Nenhum comentário para esta mensagem.")
            else:
                print(f"Mensagem {indice_mensagem + 1} não encontrada.")
        else:
            print(f"Usuário com loggin {usuario_loggin} não encontrado.")

    @staticmethod
    def contar_ocorrencias(expressao):
        ocorrencias_mensagens = 0
        ocorrencias_comentarios = 0

        for loggin, usuario in Usuario.loggins.items():
            for mensagem in usuario.mensagens:
                if expressao.lower() in mensagem['Conteudo'].lower():
                    ocorrencias_mensagens += 1

                for comentario in mensagem['comentarios']:
                    if expressao.lower() in comentario['conteudo'].lower():  # Acessar o valor correto
                        ocorrencias_comentarios += 1

        print(f"A expressão '{expressao}' ocorreu em {ocorrencias_mensagens} mensagem(s).")
        print(f"A expressão '{expressao}' ocorreu em {ocorrencias_comentarios} comentário(s).")


def mostrar_menu():
    print("\nMenu:")
    print("1. Cadastrar novo usuário")
    print("2. Excluir cadastro de usuário")
    print("3. Listar todos os usuários")
    print("4. Buscar usuário")
    print("5. Modificar dados do usuário")
    print("6. Seguir usuário")
    print("7. Deixar de seguir usuário")
    print("8. Listar seguidores de um usuário")
    print("9. Listar usuários que um usuário está seguindo")
    print("10. Exibir mensagens de um usuário e seus seguidos")
    print("11. Exibir comentários de uma mensagem específica")
    print("12. Contar ocorrências de uma expressão em mensagens e comentários")
    print("13. Mostrar usuário com mais seguidores")
    print("14. Adicionar mensagem a um usuário")
    print("15. Adicionar comentário a uma mensagem")
    print("0. Sair")

def menu():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '0':
            print("Saindo...")
            break
        
        elif escolha == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
            loggin = input("Loggin: ")
            usuario = Usuario(nome, email, data_nascimento, loggin)
            usuario.cadastrar()

        elif escolha == '2':
            loggin = input("Loggin do usuário a ser excluído: ")
            usuario = Usuario.loggins.get(loggin)
            if usuario:
                usuario.excluir_cadastro()
            else:
                print(f"Usuário com loggin {loggin} não encontrado.")

        elif escolha == '3':
            Usuario.listar_usuarios()

        elif escolha == '4':
            loggin = input("Loggin do usuário a ser buscado: ")
            usuario = Usuario.loggins.get(loggin)
            if usuario:
                usuario.search()
            else:
                print(f"Usuário com loggin {loggin} não encontrado.")

        elif escolha == '5':
            loggin = input("Loggin do usuário a ser modificado: ")
            usuario = Usuario.loggins.get(loggin)
            if usuario:
                novo_nome = input("Novo Nome: ")
                novo_email = input("Novo Email: ")
                usuario.modificar_dados(novo_nome, novo_email)
            else:
                print(f"Usuário com loggin {loggin} não encontrado.")

        elif escolha == '6':
            loggin = input("Seu loggin: ")
            usuario = Usuario.loggins.get(loggin)
            if usuario:
                seguir_loggin = input("Loggin do usuário a ser seguido: ")
                usuario.follow(seguir_loggin)
            else:
                print(f"Usuário com loggin {loggin} não encontrado.")

        elif escolha == '7':
            loggin = input("Seu loggin: ")
            usuario = Usuario.loggins.get(loggin)
            if usuario:
                unfollow_loggin = input("Loggin do usuário a ser deixado de seguir: ")
                usuario.unfollow(unfollow_loggin)
            else:
                print(f"Usuário com loggin {loggin} não encontrado.")

        elif escolha == '8':
            loggin = input("Loggin do usuário cujos seguidores serão listados: ")
            usuario = Usuario.loggins.get(loggin)
            if usuario:
                usuario.list_followers()
            else:
                print(f"Usuário com loggin {loggin} não encontrado.")

        elif escolha == '9':
            loggin = input("Loggin do usuário cujos seguidos serão listados: ")
            usuario = Usuario.loggins.get(loggin)
            if usuario:
                usuario.list_following()
            else:
                print(f"Usuário com loggin {loggin} não encontrado.")

        elif escolha == '10':
            usuario_loggin = input("Loggin do usuário: ")
            Mensagem.exibir_mensagens_usuario_e_seguidos(usuario_loggin)

        elif escolha == '11':
            usuario_loggin = input("Loggin do usuário: ")
            indice_mensagem = int(input("Índice da mensagem (0 para a primeira mensagem): "))
            Mensagem.exibir_comentarios_mensagem(usuario_loggin, indice_mensagem)

        elif escolha == '12':
            expressao = input("Digite a expressão para buscar: ")
            Mensagem.contar_ocorrencias(expressao)

        elif escolha == '13':
            Usuario.usuario_com_mais_seguidores()

        elif escolha == '14':
            loggin = input("Loggin do usuário para adicionar mensagem: ")
            usuario = Usuario.loggins.get(loggin)
            if usuario:
                conteudo = input("Conteúdo da mensagem: ")
                mensagem = Mensagem(usuario)
                mensagem.new_mensage(conteudo)
            else:
                print(f"Usuário com loggin {loggin} não encontrado.")

        elif escolha == '15':
            loggin = input("Seu loggin (quem está comentando): ")
            usuario = Usuario.loggins.get(loggin)
            if usuario:
                usuario_loggin = input("Loggin do usuário cuja mensagem será comentada: ")
                usuario_alvo = Usuario.loggins.get(usuario_loggin)
                if usuario_alvo:
                    indice_mensagem = int(input("Índice da mensagem para adicionar comentário (0 para a primeira): "))
                    comentario = input("Conteúdo do comentário: ")
                    mensagem = Mensagem(usuario_alvo)
                    mensagem.new_coment_mensage(indice_mensagem, comentario, loggin)
                else:
                    print(f"Usuário com loggin {usuario_loggin} não encontrado.")
            else:
                print(f"Usuário com loggin {loggin} não encontrado.")

        else:
            print("Opção inválida, por favor escolha uma opção válida.")

menu()
