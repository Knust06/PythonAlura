import os

restaurantes = [{'nome': 'Restaurante 1', 'categoria': 'Pizza', 'ativo': True}, {'nome': 'Restaurante 2','categoria': 'Fast-Food', 'ativo': False}, {'nome': 'Restaurante 3','categoria': 'Bar', 'ativo': True}]

def exibir_nome_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

def exibir_menu():
    '''Essa função exibe o menu principal do programa.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção inválida. Tente novamente.\n')
    voltar_menu_principal()

def main():
    '''Essa função é a principal do programa, onde é exibido o menu principal e as opções escolhidas pelo usuário.'''
    exibir_nome_programa()
    exibir_menu()
    opcao_escolhida()

def nome_opcao_escolhida(opcao_escolhida):
    '''Essa função exibe o nome da opção escolhida pelo usuário'''
    os.system('cls')
    linha = '*' * (len(opcao_escolhida))
    print(linha)
    print(opcao_escolhida)
    print(linha)

def cadastrar_restaurante():
    ''' Essa função cadastra um restaurante no sistema
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Mensagem de sucesso
    '''
    nome_opcao_escolhida('Cadastrar restaurante\n')
    nome = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do {nome}: ')
    dados = {'nome': nome, 'categoria': categoria, 'ativo': False}
    print(f'Restaurante {nome} cadastrado com sucesso na categoria {categoria}!')
    restaurantes.append(dados)
    voltar_menu_principal()

def voltar_menu_principal():
    input('\nPressione qualquer tecla para voltar ao menu principal\n')
    main()

def listar_restaurante():
    nome_opcao_escolhida('Lista de restaurantes cadastrados:')
    for i in restaurantes:
        nome_restaurante = i['nome']
        categoria_restaurante = i['categoria']
        ativo_restaurante = 'Sim' if i['ativo'] else 'Não'
        print(f'Nome: {nome_restaurante.ljust(20)} | Categoria: {categoria_restaurante.ljust(20)} | Ativo: {ativo_restaurante}')
    voltar_menu_principal()

def alternar_status_restaurante():
    nome_opcao_escolhida('Alternar status do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    for i in restaurantes:
        if i['nome'] == nome_restaurante:
            if i['ativo'] == True:
                i['ativo'] = False
                print(f'O restaurante {nome_restaurante} foi desativado.')
            else:
                i['ativo'] = True
                print(f'O restaurante {nome_restaurante} foi ativado.')
        else:
            print('Restaurante não encontrado.')
    voltar_menu_principal()

def opcao_escolhida():
    try:
        opcao_escolhida = int(input('Digite a opção desejada: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def finalizar_app():
    nome_opcao_escolhida('Finalizando aplicação...\n')
    
if __name__ == '__main__':
    main()