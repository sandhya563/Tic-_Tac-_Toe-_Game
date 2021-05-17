import random
print("\n***************************************** TIC TAC TOE GAME USER v/s COMPUTER **************************************")
print("\n                                      \U0001F600 WELCOME TO THE 'TIC TAC TOE  GAME \U0001F600\n")
player_name = input("Enter the player name:-")
print("\U0001F590  Hii",player_name," your the first player:\U0001F4BB and second player is computer \n")
def dict1():
    global board 
    board={
    '1':' ','2':' ','3':' ',
    '4':' ','5':' ','6':' ',
    '7':' ','8':' ','9':' ',
    }
def check():
################### FIRST PLAYER X #####################################

    if board['1']=='X' and board['2']=='X' and board['3']=='X' or board['4']=='X' and board['5']=='X' and board['6']=='X' or board['4']=='X' and board['5']=='X' and board['6']=='X' or board['1']=='X' and board['4']=='X' and board['7']=='X' or board['2']=='X' and board['5']=='X' and board['8']=='X' or board['3']=='X' and board['6']=='X' and board['9']=='X' or board['3']=='X' and board['5']=='X' and board['7']=='X' or board['1']=='X' and board['5']=='X' and board['9']=='X':
        print('player one won!!')
        return 1
################### SECOND PLAYER O #########################

    elif board['1']=='O' and board['2']=='O' and board['3']=='O' or board['4']=='O' and board['5']=='O' and board['6']=='O' or board['7']=='O' and board['8']=='O' and board['9']=='O' or board['1']=='O' and board['4']=='O' and board['7']=='O' or board['2']=='O' and board['5']=='O' and board['8']=='O' or board['3']=='O' and board['6']=='O' and board['9']=='O' or board['3']=='O' and board['5']=='O' and board['7']=='O' or board['1']=='O' and board['5']=='O' and board['9']=='O':
        print('player two won!!')
        return 2
    else:
        return 0
def play_game():
    dict1()
    total_moves=0
    player=1
    print("These are position which you have to choose\n")
    print("1"," |", "2 |","3")
    print("----+----+----")
    print("4"," |", "5 |","6")
    print("----+----+----")
    print("7"," |", "8 |","9\n")
    print("\U0001F600 Hii",player_name,"lets play the game \U0001F600")

    while True:
        print(board['1']+'   |'+board['2']+'   |'+board['3'])
        print("----+----+----")
        print(board['4']+'   |'+board['5']+'   |'+board['6'])
        print("----+----+----")
        print(board['7']+'   |'+board['8']+'   |'+board['9'])
        
        print("\n")
        end_check=check()
        if end_check==1:
            print("Congrats player one you are  winner!!! \U0001F600")
            break
        elif end_check==2:
            print("Congrats player two you are  winner!!! \U0001F600")
            break

        elif total_moves==9:
            print("game draw!!")
            break
        while True:
            if player==1:
                print(player_name,"Your mark is x so input your position",p1_input)
                p1_input=input("enter your position:--")
                # print(player_name,"Your mark is x so input your position",p1_input)
                if p1_input in board and board[p1_input]==' ':
                    board[p1_input]='X'
                    player=2
                    break
                else:
                    print('it is already choosed by user so you can choose other position')
                    continue
            else:
                p2_input=str(random.randint(1,9))
                print("\U0001F4BB computer choice position ",p2_input)
                if p2_input in board and board[p2_input]==' ':
                    board[p2_input]='O'
                    player=1
                    break
                else:
                    print('invalid input,please try again')
                    continue
        total_moves+=1
        print()
play_game()
def again_play():
    user_choice = input(" please enter your choice what you want \U0001F64F \n y or n :--")
    if user_choice == "y":
        play_game()
        again_play()
    else:
        print("your are exit from the game! Thank you to play \U0001F917 \U0001F917")
again_play()