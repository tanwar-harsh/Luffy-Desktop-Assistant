from IPython.display import clear_output
import random
import pyttsx3 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate",150)

def read_text(audio):
    engine.say(audio)
    engine.runAndWait()    

theBoard = [' '] * 10   
available = [str(num) for num in range(0,10)] 
players = [0,'X','O']   

def display_board(a,b):
    print('Available   TIC-TAC-TOE\n'+
           '  moves\n\n  '+
          a[7]+'|'+a[8]+'|'+a[9]+'        '+b[7]+'|'+b[8]+'|'+b[9]+'\n  '+
          '-----        -----\n  '+
          a[4]+'|'+a[5]+'|'+a[6]+'        '+b[4]+'|'+b[5]+'|'+b[6]+'\n  '+
          '-----        -----\n  '+
          a[1]+'|'+a[2]+'|'+a[3]+'        '+b[1]+'|'+b[2]+'|'+b[3]+'\n')
display_board(available,theBoard)

def display_board(a,b):
    print(f'Available   TIC-TAC-TOE\n  moves\n\n  {a[7]}|{a[8]}|{a[9]}        {b[7]}|{b[8]}|{b[9]}\n  -----        -----\n  {a[4]}|{a[5]}|{a[6]}        {b[4]}|{b[5]}|{b[6]}\n  -----        -----\n  {a[1]}|{a[2]}|{a[3]}        {b[1]}|{b[2]}|{b[3]}\n')
display_board(available,theBoard)

def place_marker(avail,board,marker,position):
    board[position] = marker
    avail[position] = ' '

def win_check(board,mark):

    return ((board[7] ==  board[8] ==  board[9] == mark) or 
    (board[4] ==  board[5] ==  board[6] == mark) or 
    (board[1] ==  board[2] ==  board[3] == mark) or
    (board[7] ==  board[4] ==  board[1] == mark) or 
    (board[8] ==  board[5] ==  board[2] == mark) or
    (board[9] ==  board[6] ==  board[3] == mark) or 
    (board[7] ==  board[5] ==  board[3] == mark) or 
    (board[9] ==  board[5] ==  board[1] == mark)) 

def random_player():
    return random.choice((-1, 1))
    
def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board[1:]

def player_choice(board,player):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            read_text('Player %s, choose your next position: (1-9) '%(player))
            position = int(input('Player %s, choose your next position: (1-9) '%(player)))
            
        except:
            read_text("I'm sorry, please try again.")
            print("I'm sorry, please try again.")
            
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

while True:
    clear_output()
    read_text('Welcome to Tic Tac Toe!')
    print('Welcome to Tic Tac Toe!')
    
    toggle = random_player()
    player = players[toggle]
    read_text('For this round, Player %s will go first!' %(player))
    print('For this round, Player %s will go first!' %(player))
    
    game_on = True
    read_text('Hit Enter to continue')
    input('Hit Enter to continue')
    while game_on:
        display_board(available,theBoard)
        position = player_choice(theBoard,player)
        place_marker(available,theBoard,player,position)

        if win_check(theBoard, player):
            display_board(available,theBoard)
            read_text('Congratulations! Player '+player+' wins!')
            print('Congratulations! Player '+player+' wins!')
            game_on = False
        else:
            if full_board_check(theBoard):
                display_board(available,theBoard)
                read_text('The game is a draw!')
                print('The game is a draw!')
                break
            else:
                toggle *= -1
                player = players[toggle]
                clear_output()

    theBoard = [' '] * 10
    available = [str(num) for num in range(0,10)]
    
    if not replay():
        break