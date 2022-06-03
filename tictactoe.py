
#tictactoe game

def board_print_first():
    a=[0,1,2,3,4,5,6,7,8,9]
    print(f"| {a[7]} | {a[8]} | {a[9]} |\n-------------\n| {a[4]} | {a[5]} | {a[6]} |\n-------------\n| {a[1]} | {a[2]} | {a[3]} |")
def initial_start():
    name=None
    print('Hello and welcome to my TicTacToe game!')
    name = input('what is your name? ')
    print(f'Great {name}, let me Show you the board, its like the numpad that you are used too')
    board_print_first()
    print('The rules are really simple, each player takes his turn and selects the position and the X or O')

#________________________________________________
tictactoe_board = {7: 7 ,8: 8 ,9: 9 ,4: 4 ,5: 5 ,6: 6 ,1: 1 ,2: 2 ,3: 3 }
prev_turn= ['empty'] 
prev_pos = [0]

def the_board(position, mark):
    tictactoe_board[position] = mark
    print(f"| {tictactoe_board[7]} | {tictactoe_board[8]} | {tictactoe_board[9]} |\n-------------\n| {tictactoe_board[4]} | {tictactoe_board[5]} | {tictactoe_board[6]} |\n-------------\n| {tictactoe_board[1]} | {tictactoe_board[2]} | {tictactoe_board[3]} |")
    winner(mark)
    user_input()

def prev_turn_checker(position):
    for num in prev_pos:
        if  int(num) == int(position):
            print(f'Sorry bud the slot {position} already taken')
            return False
    return True

def user_input():
    check_avilablity()
    while True:
        position = input("Insert the position that you want it to be: ")  
        if 1<= int (position) <=9 and prev_turn_checker(position):
            mark = input('choose X or O: ')
            if mark == 'x' or mark == 'X' or mark == 'o' or mark == 'O':
                if prev_turn[-1] == mark:
                    print(f'You already went last turn with {mark} try the other one')
                else:
                    prev_turn.append(mark.lower())
                    prev_pos.append(position)
                    return the_board(int(position), mark.lower())         
            else:
                print('try again')
        else:
            print('try again')

def check_avilablity():
    for value in tictactoe_board.values():
        if type(value) == type(1):    
            return True
    print("There is no moves left.")  

def winner(mark):
    win_lst=[]
    for value in tictactoe_board.values():
        win_lst.append(value)
    if win_lst[0] == win_lst[1] == win_lst[2] or win_lst[3] == win_lst[4] == win_lst[5] or win_lst[6] == win_lst[7] == win_lst[8] or win_lst[0] == win_lst[3] == win_lst[6] or win_lst[1] == win_lst[4] == win_lst[7] or win_lst[2] == win_lst[5] == win_lst[8] or win_lst[0] == win_lst[4] == win_lst[8] or win_lst[2] == win_lst[4] == win_lst[6]:
        print(f'{mark} won the game! congrats!')
        conti()
    else:
        False

def conti():
    answer = input("Do you want to continue? write down 'yes' or 'no'")
    if answer == "yes":
        user_input()
    else:
        quit()

def main():
    initial_start()
    user_input()

main()