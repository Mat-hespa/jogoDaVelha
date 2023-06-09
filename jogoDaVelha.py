vazio = " "
XorO = ["X", "O"]

def criaBoard():
    board = [
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
    ]
    return board

def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if(i < 2):
            print("-----")


def getInputValido(msg):
    try:
        n = int(input(msg))
        if(n >= 1 and n <= 3):
            return n - 1
        else:
            print("Numero entre 1 e 3")
            return getInputValido(msg)
    except:
        print("Nao valido")
        return getInputValido(msg)

def verificaMovimento(board, i , j):
    if(board[i][j] == vazio):
        return True
    else:
        return False

def fazMovimento(board, i, j, jogador):
    board[i][j] = XorO[jogador]

def verificaGanhador(board):
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != vazio):
            return board[i][0]
    for i in range(3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != vazio):
            return board[0][i]
    if(board[0][0] != vazio and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]
    if(board[0][2] != vazio and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]
    for i in range(3):
        for j in range(3):
            if(board[i][j] == vazio):
                return False
    return "Empatou"
