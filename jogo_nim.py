def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        for i in range(1, m+1):
            if (n - i) % (m + 1) == 0:
                return i
        return m

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada <= 0 or jogada > m or jogada > n:
        print("Jogada inválida! Tente novamente.")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        print("Você começa!")
        jogador = 1
    else:
        print("Computador começa!")
        jogador = 0
    
    while n > 0:
        if jogador == 0:
            jogada = computador_escolhe_jogada(n, m)
            print("O computador tirou", jogada, "peças.")
            n -= jogada
            jogador = 1
        else:
            jogada = usuario_escolhe_jogada(n, m)
            print("Você tirou", jogada, "peças.")
            n -= jogada
            jogador = 0
        
        print("Agora restam", n, "peças no tabuleiro.")
    
    if jogador == 0:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    for _ in range(3):
        print("**** Rodada", _+1, "****")
        vencedor = partida()
        if vencedor == "Você":
            placar_usuario += 1
        else:
            placar_computador += 1
    
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - Partida única")
    print("2 - Campeonato")
    escolha = int(input())
    if escolha == 1:
        print("Você escolheu partida única!")
        partida()
    elif escolha == 2:
        print("Você escolheu campeonato!")
        campeonato()
    else:
        print("Escolha inválida!")

if __name__ == "__main__":
    main()
