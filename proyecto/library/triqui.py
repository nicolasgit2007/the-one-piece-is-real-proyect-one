def main_triqui():
    board = [[[0,0,0],
               [0,0,0],
               [0,0,0]],
                        [[0,0,0],
                         [0,0,0],
                         [0,0,0]],
                                  [[0,0,0],
                                   [0,0,0],
                                   [0,0,0]]]
    def win(board,pieza):
        
        if board[0] == [pieza]*3:
            return True
        if board[0][0][0]==pieza and board[1][0][0] == pieza and board[2][0][0]==pieza:
            return True
        if board[0][0][1]==pieza and board[1][0][1] == pieza and board[2][0][1]==pieza:
            return True
        if board[0][0][2]==pieza and board[1][0][2] == pieza and board[2][0][2]==pieza:
            return True
        if board[0][1][0]==pieza and board[1][1][0] == pieza and board[2][1][0]==pieza:
            return True
        if board[0][1][1]==pieza and board[1][1][1] == pieza and board[2][1][1]==pieza:
            return True
        if board[0][1][2]==pieza and board[1][1][2] == pieza and board[2][1][2]==pieza:
            return True
        if board[0][2][0]==pieza and board[1][2][0] == pieza and board[2][2][0]==pieza:
            return True
        if board[0][2][1]==pieza and board[1][2][1] == pieza and board[2][2][1]==pieza:
            return True
        if board[0][2][2]==pieza and board[1][2][2] == pieza and board[2][2][2]==pieza:
            return True
        if board[0][0][0]==pieza and board[0][0][1] == pieza and board[0][0][2]==pieza:
            return True
        if board[0][0][0]==pieza and board[0][1][1] == pieza and board[0][2][2]==pieza:
            return True
        if board[0][0][0]==pieza and board[0][1][0] == pieza and board[0][2][0]==pieza:
            return True
        if board[0][0][1]==pieza and board[0][1][1] == pieza and board[0][2][1]==pieza:
            return True
        if board[0][0][2]==pieza and board[0][1][2] == pieza and board[0][2][2]==pieza:
            return True
        if board[0][1][0]==pieza and board[0][1][1] == pieza and board[0][1][2]==pieza:
            return True
        if board[0][2][0]==pieza and board[0][2][1] == pieza and board[0][2][2]==pieza:
            return True
        if board[1][0][0]==pieza and board[1][0][1] == pieza and board[1][0][2]==pieza:
            return True
        if board[1][0][0]==pieza and board[1][1][1] == pieza and board[1][2][2]==pieza:
            return True
        if board[1][0][0]==pieza and board[1][1][0] == pieza and board[1][2][0]==pieza:
            return True
        if board[1][0][1]==pieza and board[1][1][1] == pieza and board[1][2][1]==pieza:
            return True
        if board[1][0][2]==pieza and board[1][1][2] == pieza and board[1][2][2]==pieza:
            return True
        if board[1][1][0]==pieza and board[1][1][1] == pieza and board[1][1][2]==pieza:
            return True
        if board[1][2][0]==pieza and board[1][2][1] == pieza and board[1][2][2]==pieza:
            return True
        if board[2][0][0]==pieza and board[2][0][1] == pieza and board[2][0][2]==pieza:
            return True
        if board[2][0][0]==pieza and board[2][1][1] == pieza and board[2][2][2]==pieza:
            return True
        if board[2][0][0]==pieza and board[2][1][0] == pieza and board[2][2][0]==pieza:
            return True
        if board[2][0][1]==pieza and board[2][1][1] == pieza and board[2][2][1]==pieza:
            return True
        if board[2][0][2]==pieza and board[2][1][2] == pieza and board[2][2][2]==pieza:
            return True
        if board[2][1][0]==pieza and board[2][1][1] == pieza and board[2][1][2]==pieza:
            return True
        if board[2][2][0]==pieza and board[2][2][1] == pieza and board[2][2][2]==pieza:
            return True
        
        return False 
    def print_board(board):
        for b in board:
            print("======")
            for i in b:
                print(i)
    piezas = ["X","O"]
    turno = 0
    while True:
        x, y, z =map (int,input().split())
        
        if board[x][y][z] != 0:
            ...
        else:
            board[x][y][z] = piezas[turno%2]
            print_board(board)
            
            if win(board, piezas[turno%2]):
                print(f"HA GANADO {piezas[turno%2]}")
                break
            turno += 1