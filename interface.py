import PySimpleGUI as sg #necessario instalar a biblioteca 
from cadastro import *


def login():
    """Função que define o estilo da janela de login"""
    estilo = [
        [sg.Text('Nome:', size=5), sg.Input(key='nome', size=15)],
        [sg.Text('Senha:', size=5), sg.Input(key='senha', size=15)],
        [sg.Button('Entrar', size=6, ), sg.Button('criar', size=6)],
        [sg.Text('', key='confirmacao')]
    ]

    return sg.Window('login', layout=estilo, finalize=True)


janela1 = login()


while True: 
    """looping responsável por deixar a janela sempre rodando.
    Todas os eventos que acontecem na interface são lidos por conta do looping"""
    window, event, values = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED:
        break

    elif window == janela1 and event == 'criar':
        nome = values['nome']
        senha = values['senha']

        if len(nome) == 0:
            janela1['confirmacao'].update('Digite um nome')
        elif len(senha) == 0:
            janela1['confirmacao'].update('Digite uma senha')
        else:
            janela1['confirmacao'].update('Cadastro feito com sucesso')
            cadastrar(nome, senha)
        
    else:
        nome = values['nome']
        senha = values['senha']

        if len(nome) == 0:
            janela1['confirmacao'].update('Digite um nome')
        elif len(senha) == 0:
            janela1['confirmacao'].update('Digite uma senha')
        else:
            conta_cadastrada = entrar(nome, senha)
            janela1['confirmacao'].update('entrou com sucesso' if conta_cadastrada == True else 'Cadastro não encontrado')
