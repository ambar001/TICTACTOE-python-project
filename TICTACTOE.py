
def boardprint(tbl):
  
    print(f" {tbl[0]} | {tbl[1]} | {tbl[2]} ")
    print(f"---|---|---")
    print(f" {tbl[3]} | {tbl[4]} | {tbl[5]} ")
    print(f"---|---|---")
    print(f" {tbl[6]} | {tbl[7]} | {tbl[8]} ")

def chkwin(tbl):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
  
        if(tbl[win[0]] == tbl[win[1]] == tbl[win[2]] == 'O'):
            boardprint(tbl)
            print("O Won the match")
            return 0
        
        if(tbl[win[0]] == tbl[win[1]] == tbl[win[2]] == 'X'):
            boardprint(tbl)
            print("X Won the match")
            return 1
     
        if all(isinstance(item, str) for item in tbl):
            boardprint(tbl)
            return -2
    return -1


print("lets play Tic Tak Toe")
tbl=[0, 1, 2, 3, 4, 5, 6, 7, 8]
turn = 1

while(True):
    try:
        if turn == 1:
            boardprint(tbl)
            print("\n person1 turn")
            value = int(input("\nenter number of place "))

            if tbl[value]!= 'O':
                tbl[value] = 'X'
            

        if turn == 0:
            boardprint(tbl)
            print("\n person2 turn\n")
            value = int(input("\nenter number of place "))

            if tbl[value]!= 'X':
               tbl[value] = 'O'
            
    except IndexError:
        print("\n enter value from 1-8\n")
        continue
    turn = 1 - turn
    wonn = chkwin(tbl)
    if(wonn!=-1):
        print("Match over")
        break
    if(wonn==-2):
        print("Game Draw")
        break
   
    