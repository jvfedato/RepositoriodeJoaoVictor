from funcoes import define_posicoes, preenche_frota, posicao_valida, posiciona_frota, faz_jogada, afundados, monta_tabuleiros

frota = {}

tamanhos = {
    "porta-aviões": [1, 4],
    "navio-tanque": [2, 3],
    "contratorpedeiro": [3, 2],
    "submarino": [4, 1],
}

for nome in tamanhos:
    quantidade = tamanhos[nome][0]
    tamanho = tamanhos[nome][1]
    for i in range(quantidade):
        while True:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome == "submarino":
                orientacao = "horizontal"
            else:
                resposta = int(input("Orientação: [1] Vertical [2] Horizontal "))
                if resposta == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break
            else:
                print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogadas = []
jogando = True
mostrar_tabuleiro = True

while jogando:
     if mostrar_tabuleiro:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
        linha = int(input("Jogador, qual linha deseja atacar? "))
        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))
        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))
        if [linha, coluna] in jogadas:
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
            mostrar_tabuleiro = False
        else:
         jogadas.append([linha,coluna])
         tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
         mostrar_tabuleiro = True
         if afundados(frota_oponente, tabuleiro_oponente) == 10:
            print("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False


