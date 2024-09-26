import random
import time
import json
import os


times = [
        {'nome': 'Ituano', 'forca': 11.7},
        {'nome': 'Mirassol', 'forca': 13.8},
        {'nome': 'Ceará', 'forca': 13.5},
        {'nome': 'Goiás', 'forca': 13.8},
        {'nome': 'Sport', 'forca': 14.8},
        {'nome': 'Santos', 'forca': 15.5},
        {'nome': 'Amazonas', 'forca': 11.9},
        {'nome': 'América Mineiro', 'forca': 13},
        {'nome': 'Avaí', 'forca': 12},
        {'nome': 'Botafogo-SP', 'forca': 11.4},
        {'nome': 'Brusque', 'forca': 10.6},
        {'nome': 'Chapecoense', 'forca': 10.4},
        {'nome': 'Coritiba', 'forca': 12.5},
        {'nome': 'CRB', 'forca': 11.1},
        {'nome': 'Guarani', 'forca': 10.2},
        {'nome': 'Novorizontino', 'forca': 14.4},
        {'nome': 'Operário', 'forca': 11.6},
        {'nome': 'Paysandu', 'forca': 10.8},
        {'nome': 'Ponte Preta', 'forca': 10.8},
         {'nome': 'Vila Nova', 'forca': 13.7}

]

tabela = {time['nome']: {'pontos': 0, 'jogos': 0, 'vitorias': 0, 'empates': 0, 'derrotas': 0, 'saldo_gols': 0} for time in times}

def salvartabela(tabela):
    caminho = os.path.join(os.getcwd(), 'tabela_classificacao.json')
    with open(caminho, 'w') as f:
        json.dump(tabela, f)
        print(f'Tabela salva com sucesso em {caminho}')


def simulacao():
    
    casa, fora = random.sample(times, 2)

    chance_casa = casa['forca'] + random.uniform (1, 8)
    chance_fora = fora['forca'] + random.uniform (1, 8)




    casa['forca'] += 2

    placarcasa = random.randint (1, 5)
    placarfora = random.randint (1, 5)


    print(f'Simulando a partida entre {casa["nome"]} (Casa) e {fora["nome"]} (Fora)...')
    time.sleep(2)
    print('.')
    time.sleep(0.7)
    print('..') 
    time.sleep(0.7)
    print('...')

    if chance_casa > chance_fora:
        placarcasa = random.randint (1, 5)
        placarfora = random.randint (0, placarcasa -1)

        tabela[casa['nome']]['pontos'] += 3
        tabela[casa['nome']]['vitorias'] += 1
        tabela[casa['nome']]['saldo_gols'] += placarcasa - placarfora
        tabela[casa['nome']]['jogos'] += 1

        tabela[fora['nome']]['derrotas'] += 1
        tabela[fora['nome']]['saldo_gols'] += placarfora - placarcasa
        tabela[fora['nome']]['jogos'] += 1


        print(f'O {casa["nome"]} venceu a partida! Placar: {placarcasa}x{placarfora}')


    elif chance_casa < chance_fora:
                
        placarfora = random.randint (1, 5)
        placarcasa = random.randint (0, placarfora -1)

        tabela[fora['nome']]['pontos'] += 3
        tabela[fora['nome']]['vitorias'] += 1
        tabela[fora['nome']]['saldo_gols'] += placarfora - placarcasa
        tabela[fora['nome']]['jogos'] += 1

        tabela[casa['nome']]['derrotas'] += 1
        tabela[casa['nome']]['saldo_gols'] += placarcasa - placarfora
        tabela[casa['nome']]['jogos'] += 1

        print(f'O {fora["nome"]} venceu a partida! Placar: {placarcasa}x{placarfora}')
        print('Agora a tabela é:')
        
        print(f'1. {fora["nome"]} 3 Pontos')
        print (f'2. {casa["nome"]} 0 Pontos')
    else:

        placarcasa = random.randint (1, 5)

        tabela[fora['nome']]['pontos'] += 1
        tabela[fora['nome']]['empates'] += 1
        tabela[fora['nome']]['saldo_gols'] += placarfora - placarcasa
        tabela[fora['nome']]['jogos'] += 1

        tabela[casa['nome']]['pontos'] += 1
        tabela[casa['nome']]['empates'] += 1
        tabela[casa['nome']]['saldo_gols'] += placarfora - placarcasa
        tabela[casa['nome']]['jogos'] += 1

        print(f'O jogo terminou empatado! Placar: {placarcasa}x{placarcasa}')

        salvartabela(tabela)


    





simulacao()
