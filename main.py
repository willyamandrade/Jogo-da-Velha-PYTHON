from random import randrange, choice

jogador = 1 # jogador X = 1, jogador O = -1
tabuleiro = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print("\n")
print(len("JOGO DA VELHA") * "#")
print("JOGO DA VELHA")
print(len("JOGO DA VELHA") * "#")

def convSimbJogador():
    if jogador == 1:
        return "X"
    else:
        return "O"   
    
def mostrarTabuleiro():
    print("\n")
    print("Turno do Jogador", simbJogador)
    print("A | B | C |")
    print(11 * "=")
    for i in range(len(tabuleiro)):
        print(f"{tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} | {i+1}")
        if i != 2:
            print(11 * "-")
            
def convLetraNum(letra):
    # Converte a letra em seu respectivo número
    conv = {"A" : 0, "B" : 1, "C" : 2}
    return conv[letra]

def proxTurno():
    global jogador
    jogador *= -1
    
def jogada():
    while True:
        mostrarTabuleiro()
        exemploLetra = choice(['A', 'B', 'C'])
        exemploNumero = randrange(1, 4)
        print("\n")
        print(f"Exemplo de jogada: {exemploLetra}{exemploNumero}")

        try:
            jogada = input("Digite um espaço para jogar: ").upper()
            letraTab = convLetraNum(jogada[0])
            numTab = int(jogada[1]) - 1 
        except:
            print("ERRO: Jogada incorreta. Siga o formato de exemplo de jogada.")
            continue

        if letraTab not in range(3) or numTab not in range(3) or len(jogada) > 2:
            print("ERRO: Jogada incorreta. Siga o formato de exemplo de jogada.")
            continue
        
        elif tabuleiro[numTab][letraTab] != "-":
            print("ERRO: Este espaço está ocupado.")
            continue
        
        tabuleiro[numTab][letraTab] = simbJogador

        return

def checVitoria():
    mostrarTabuleiro()
    for i in range(3): # CHECAGEM HORIZONTAL
        if tabuleiro[i] == [simbJogador, simbJogador, simbJogador]:
            return True
    for i in range(3): # CHECAGEM VERTICAL
        if tabuleiro[0][i] == simbJogador and tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[0][i] == tabuleiro[2][i]:
            return True
    for i in range(0,3,2): # CHECAGEM DIAGONAL
        if tabuleiro[0][i] == simbJogador and tabuleiro[0][i] == tabuleiro[1][1] and tabuleiro[0][i] == tabuleiro[2][2-i]:
            return True

def checEmpate():
    mostrarTabuleiro()
    if "-" not in tabuleiro[0]:
        if "-" not in tabuleiro[1]:
            if "-" not in tabuleiro[2]:
                    return True
    return False

def recomecar():
    recomeco = "a"

    while recomeco != "s" and recomeco != "n":
        try:
            recomeco = input("Jogar novamente? (s/n): ").lower()
        except:
            print("ERRO: Use as letras do teclado.")

        if recomeco != "s" and recomeco != "n":
            print("\nERRO: Insira uma opção válida.")
            print("sim = s, não = n\n")
            continue

    if recomeco == "s":
        global tabuleiro
        global jogador
        jogador = 1 
        tabuleiro = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        return True

    elif recomeco == "n":
        return False

while True:
    simbJogador = convSimbJogador()
    jogada()

    if checVitoria() == True:
        print("\n", simbJogador, "Venceu!\n")
        if recomecar() == False:
            break
    elif checEmpate() == True:
        print("\n Empate!\n")
        if recomecar() == False:
            break
    else:
        proxTurno()

print("\nFim do Programa")