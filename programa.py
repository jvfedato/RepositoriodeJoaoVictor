from funcoes import define_posicoes, preenche_frota, posicao_valida

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
                resposta = int(input("[1] Vertical [2] Horizontal >"))
                if resposta == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break
            else:
                print("Esta posição não está válida!")
print(frota)
