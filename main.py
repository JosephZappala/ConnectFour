from flask import Flask, request, render_template

app = Flask(__name__)

global turn1
turn1 = True
global turn
turn = ""

global playRname
global playYname
global userName
global fileName
fileName = "buff"
userName = ""

winner = ""

game = [['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0']]


def checkRWin(board):
    boardHeight = len(board[0])
    boardWidth = len(board)
    tile = 'R'
    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == tile and board[x + 1][y] == tile and board[x + 2][y] == tile and board[x + 3][y] == tile:
                return True

    # check vertical spaces
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == tile and board[x][y + 1] == tile and board[x][y + 2] == tile and board[x][y + 3] == tile:
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == tile and board[x + 1][y - 1] == tile and board[x + 2][y - 2] == tile and board[x + 3][
                y - 3] == tile:
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == tile and board[x + 1][y + 1] == tile and board[x + 2][y + 2] == tile and board[x + 3][
                y + 3] == tile:
                return True

    return False


def checkYWin(board):
    boardHeight = len(board[0])
    boardWidth = len(board)
    tile = 'Y'
    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == tile and board[x + 1][y] == tile and board[x + 2][y] == tile and board[x + 3][y] == tile:
                return True

    # check vertical spaces
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == tile and board[x][y + 1] == tile and board[x][y + 2] == tile and board[x][y + 3] == tile:
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == tile and board[x + 1][y - 1] == tile and board[x + 2][y - 2] == tile and board[x + 3][
                y - 3] == tile:
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == tile and board[x + 1][y + 1] == tile and board[x + 2][y + 2] == tile and board[x + 3][
                y + 3] == tile:
                return True

    return False


def checkIfBoardIsFull(board):
    boardHeight = len(board[0])
    boardWidth = len(board)
    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if (board[x][y] != 'R' and board[x][y] != 'Y'):
                return False
    return True


global reset
reset = False


def resetGameConnect():
    global game
    global reset
    global winner
    global turn1
    game = [['0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0']]
    reset = False
    turn1 = not turn1
    winner = ""


def loadGameConnect(fileName):
    global game
    global playYname
    global playRname
    global turn1
    global turn
    try:
        gameFile = open(fileName, 'r')
        playRname = gameFile.readline()
        playRname = playRname[:len(playRname) - 1]
        playYname = gameFile.readline()
        playYname = playYname[:len(playYname) - 1]
        gameStore = gameFile.readline()
        locOfGameStore = 0
        game = [['0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0']]
        for i in range(0, 6):
            for j in range(0, 7):
                game[i][j] = gameStore[locOfGameStore]
                locOfGameStore += 1
        turn1Store = gameFile.readline()
        if turn1Store == '1':
            turn = playRname + "'s turn"
            turn1 = True
        else:
            turn = playYname + "'s turn"
            turn1 = False
        gameFile.close()
        return True
    except:
        print(fileName, "dosent exist")
        resetGameConnect()
        turn = "That game does not exist"
        return False


def saveGameConnect(fileName):
    global game
    global playYname
    global playRname
    global turn1
    gameFile = open(fileName, 'w')
    gameFile.write(playRname)
    gameFile.write("\n")
    gameFile.write(playYname)
    gameFile.write("\n")
    gameStore = ""
    for i in range(0, 6):
        for j in range(0, 7):
            gameStore += game[i][j]
    gameFile.write(gameStore)
    gameFile.write("\n")
    if turn1:
        turnString = "1"
    else:
        turnString = "0"
    gameFile.write(turnString)
    gameFile.close()


def playConnect(col):
    global reset
    global winner
    global turn1
    global turn
    global userName
    global fileName
    global playRname
    global playRname
    if not loadGameConnect(fileName):
        return
    if reset:
        resetGameConnect()
    piece = '0'
    if turn1 and userName == playRname:
        turn1 = False
        piece = 'R'
        turn = playYname + "'s turn"
    elif (not turn1) and userName == playYname:
        turn1 = True
        piece = 'Y'
        turn = playRname + "'s turn"
    if userName != "":
        for i in range(5, -1, -1):
            if game[i][col] != 'R' and game[i][col] != 'Y':
                game[i][col] = piece
                break
    # displayGame()
    if checkIfBoardIsFull(game):
        winner = "It was a draw"
        reset = True
    if not turn1:
        if checkRWin(game):
            # print("The winner is Red")
            winner = "The winner is Red"
            reset = True
    if turn1:
        if checkYWin(game):
            # print("The winner is Yellow")
            winner = "The winner is Yellow"
            reset = True
    saveGameConnect(fileName)
    return


@app.route('/makeNewGame', methods=['GET', 'POST'])
def makeNewGame():
    data = request.form
    if bool(data):
        if 'newGame' in data.keys():
            # print(data['post'])
            if ' ' in data['newGame']:
                data = data['newGame']
                data = data.split(' ')
                print(data)
                fileName = data[0] + data[3] + ".txt"
                player1 = data[1]
                player2 = data[2]
                try:
                    gameFile = open(fileName, 'x')
                    gameFile.write(player1)
                    gameFile.write("\n")
                    gameFile.write(player2)
                    gameFile.write("\n")
                    gameStore = ""
                    if data[3] == "ConnectFour":
                        for i in range(0, 6):
                            for j in range(0, 7):
                                gameStore += '0'
                    if data[3] == "TicTacToe":
                        for i in range(0, 3):
                            for j in range(0, 3):
                                gameStore += '0'
                    gameFile.write(gameStore)
                    gameFile.write("\n")
                    turnString = "1"
                    gameFile.write(turnString)
                    gameFile.close()
                except:
                    print("Game Code Already Exists")

    return index()


def playTicTacToe(loc):
    row = loc / 10
    col = loc % 10


@app.route('/', methods=['GET', 'POST'])
def index():
    global userName
    global fileName
    global turn
    data = request.form
    if bool(data):
        if 'post' in data.keys():
            # print(data['post'])
            if ' ' in data['post']:
                data = data['post'].split(' ')
                userName = data[0]
                fileName = data[2]
                # print(userName)
            # print(data['post'][len(data['post']) - 1])
            # print(int(data['post'][data['post'].index(' ') + 1]) - 1)
            if data[3] == 'ConnectFour':
                playConnect(int(data[1]) - 1)
    return render_template('ConnectFour.html', data=game, dataWin=winner, _external=True, dataTurn=turn)


@app.route('/refresh', methods=['GET', 'POST'])
def refresh():
    return index()


@app.route('/load-game', methods=['GET', 'POST'])
def postLoadGameConnect():
    # print(request.form['game_name'])

    loadGameConnect(request.form['game_name'] + "ConnectFour.txt")
    return index()


if __name__ == '__main__':
    # type in hosts IP
    app.run(host='---.--.---.---', port=8000, debug=False)
