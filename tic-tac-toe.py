import os
import pyttsx3
import random
os.system('cls')
e=pyttsx3.init()
sy = pyttsx3.speak
e.setProperty('rate', 170)

z = [1,2,3,4,5,6,7,8,9]
l = [1,2,3,4,5,6,7,8,9]
m = [1,2,3,4,5,6,7,8,9]
no=[]
q=0
sound="hay!, let's play tic tac toe, select the number where you want to put x"
def game2(m):
     p=0
     while p<9:
        if m[p]!="O" and m[p]!="X":
            m[p]=" "
        p=p+1
     print(f"\n {m[0]}   |   {m[1]}   |   {m[2]}\n-------------------\n {m[3]}   |   {m[4]}   |   {m[5]}\n-------------------\n {m[6]}   |   {m[7]}   |   {m[8]}\n")

def game(l):
     print(f"\n {l[0]}   |   {l[1]}   |   {l[2]}\n-------------------\n {l[3]}   |   {l[4]}   |   {l[5]}\n-------------------\n {l[6]}   |   {l[7]}   |   {l[8]}\n")

def menu(x,l): 
    global q
    if l[0]==l[1]==l[2]==x or l[3]==l[4]==l[5]==x or l[6]==l[7]==l[8]==x or l[0]==l[3]==l[6]==x or l[1]==l[4]==l[7]==x or l[2]==l[5]==l[8]==x or l[0]==l[4]==l[8]==x or l[2]==l[4]==l[6]==x:
        os.system("cls") 
        game2(m)  
        print(f"game over\n{x} win\n")
        if x=="X":
            sy("well done, you won")
        else: sy("ha ha ha... better luck next time")
        print("enter q for QUIT and r for RESTART :", end=" ")
        sy("or you want to quit")
        user=input().lower()
        if user=="q":
            sy("ok,we shell play later")
            q=1
        elif user=="r":
            l[:] = [1,2,3,4,5,6,7,8,9]  
            m[:] = [1,2,3,4,5,6,7,8,9]
            no.clear()
            game(l)
            sound="nice! lets play again"
            sy(sound)
            return
    if (l[0]=="O" or l[0]=="X") and (l[1]=="O" or l[1]=="X") and (l[2]=="O" or l[2]=="X") and (l[3]=="O" or l[3]=="X") and (l[4]=="O" or l[4]=="X") and (l[5]=="O" or l[5]=="X") and (l[6]=="O" or l[6]=="X") and (l[7]=="O" or l[7]=="X") and (l[8]=="O" or l[8]=="X"):
        print("DRAW")
        sy("oh,it's draw, we can try again")
        print("enter q for QUIT and r for RESTART :", end=" ")
        sy("or you want to quit")
        user=input().lower() 
        if user=="q":
            print("Thanks..! for playing")
            sy("ok,we shell play later")
            q=1
        elif user=="r":
            l[:] = [1,2,3,4,5,6,7,8,9]  
            m[:] = [1,2,3,4,5,6,7,8,9]
            game(l)
            sound="nice! lets play again"
            sy(sound)
game(l)
game2(m)
print("hay!, let's play tic tac toe, select the number where you want to put x")
sy(sound)
while q==0:
    os.system("cls") 
    game(l)
    game2(m)
    while (True):
        x=int(input("\nX turn : "))
        if x not in no :
            no.append(x)
            l[x-1]="X"
            m[x-1]="X"
            menu("X",l)
            break
        else: 
            print("ERROR : (possition occupied)\nPLEASE TRY AGAIN")
            sy("used hai, kuch or try karo")
    n=0
    while (True):
       y=random.choice(z)
       if y not in no :
           if y==l[n]:
            l[n]="O"
            m[n]="O"
            menu("O",l)
            if q==1:
                break
            no.append(y)
            break
       else: n=n+1
       if n==9:
           n=0
