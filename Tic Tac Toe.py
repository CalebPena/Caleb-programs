p=[" "," "," "," "," "," "," "," "," ",]
possible=["tl","tm","tr","ml","mm","mr","bl","bm","br"]
k=0
bar="-+-+-"
turn="x"
wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def board():
    print(p[0]+"|"+p[1]+"|"+p[2])
    print(bar)
    print(p[3]+"|"+p[4]+"|"+p[5])
    print(bar)
    print(p[6]+"|"+p[7]+"|"+p[8])
def changeTurn():
    global turn
    if turn=="x":
        turn="o"
    elif turn=="o":
        turn="x"
def move():
    if mov in possible:
        index=possible.index(mov)
        if p[index]==" ":
            p[index]=turn
            changeTurn()
        else:
            print("invaled input")
    else:
        print("invaled input")

def win():
    global k
    u=0
    while u<len(wins):
        if p[wins[u][0]]=="x" or p[wins[u][0]]=="o":
            if p[wins[u][0]]==p[wins[u][1]] and p[wins[u][0]]==p[wins[u][2]]:
                print(p[wins[u][0]]+" wins")
                k+=1
                break
        u+=1
def draw():
    d=0
    global k
    for i in p:
        if i=="x" or i=="o":
            d+=1
    if d==9:
        print("draw")
        k+=1
board()
while k==0:
    print("it is "+turn+"'s turn")
    mov=input("where do you want to go: ")
    move()
    board()
    win()
    if k==0:
        draw()
