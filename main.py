from jogoDaVelha import *
from minimax import *

jogador = 0
board = criaBoard()
ganhador = verificaGanhador(board)

while(not ganhador):
    
    printBoard(board)
    print("******************************")
    
    if(jogador == 0):
        i,j = movimentoIA(board, jogador)
    else:
        i,j = movimentoIA(board, jogador)
        i = getInputValido("Digite a linha: ")
        j = getInputValido("Digite a coluna: ")
    
    if(verificaMovimento(board, i, j)):
        fazMovimento(board, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("Posição ocupada")
    
    ganhador = verificaGanhador(board)

print()
printBoard(board)
print()
print("Ganhador = ", ganhador)
