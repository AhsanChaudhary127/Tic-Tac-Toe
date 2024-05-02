from os import system

global n
global arr
global game
global pl1
global pl2

n = "\n"
pl1 = []
pl2 = []

def clear():
    if __name__ == "__main__":
        system('cls')
    else:
        system('clear')

arr = [[0,0,0],
       [0,0,0],
       [0,0,0]]

game = [["-","-","-"],
       ["-","-","-"],
       ["-","-","-"]]

def player(x):
    if x % 2 == 0:
        return(1)
    else:
        return(2)
    
def win():
    x = open("cond.txt",'r')
    for i in range(8):
        y = x.readline()
        y = y.strip()
        y = y.split(",")
        if y[0] in pl1 and y[1] in pl1 and y[2] in pl1:
            win = 1
            break
        elif y[0] in pl2 and y[1] in pl2 and y[2] in pl2:
            win = 2
            break
        else:
            win = 3
            continue
    return win
    
def main():
    clear()
    loop = 0
    while True:
        
        for i in game:
            for j in i:
                print(j,"   ",end="")
            print("\n")
            
        current = player(loop)
        
        if current == 1:
            sign = "O"
        else:
            sign = "X"
            
        print(f"Current Player : Player {current} ({sign})")
        
        inp = ''
        while inp != 'a' or inp != 'b' or inp != 'c':
            inp = input("Enter Column (a,b,c): ")
            if inp == 'a' or inp == 'b' or inp == 'c':
                break
            else: 
                print(('Please Enter Correct Column(a,b,c)'))
        inp2 = 0        
        while inp2 <= 0 or inp2 >= 4:
            inp2 = int(input("Enter Row (1,2,3): "))
            if inp2 < 4 and inp2 > 0:
                break
            else:
               print(('Please Enter Correct Row(1,2,3)')) 
               
        move = inp + str(inp2)
        
        if current == 1:
            pl1.append(move)
        else:
            pl2.append(move)
        
        col = {
            "a" : 0,
            "b": 1,
            "c" : 2
        }
        
        idx2 = inp2 - 1
        idx = col.get(inp)
            
        if arr[idx2][idx] == 1:
            clear()
            print("Please select another postion")

            continue
        else:
            arr[idx2][idx] = 1
            game[idx2][idx] = sign
            loop += 1
            
        winner = win()
        if winner == 3:
            clear()
            continue
        else:
            clear()
            for i in game:
                for j in i:
                    print(j,"   ",end="")
                print("\n")
            
            print(f'Player {current} Wins !')
            break
        
        
        



main()