# Carlos Antonio Flores Delgado

f = 1000
e = 100
i = 0
z =1
m = 0

while z == 1:
    print("What is the amount of water(L) in the lake?")
    print("Current: Full", f, " Empty", e )
    i = int(input(">"))
    if i >= f:
        f = i
    elif i <= e:
        e = i
        
    t = int(f+e)
    m = int((f+e)/2)
    ae = int((t * .25)-e)
    af = int((t * .75)-e)
    aep = int((t * .35)-e)
    mp = int((t * .65)-e)
    afp = int((t * .99)-e)
    print("full:",f," amost full:", af," middle:", m," almost empty:", ae," empty:", e)

    if i == e:
        print("the lake is emty")
    elif i <= aep:
        print("the lake is almost empty")
    elif i <= mp:
        print("the lake is the middle")
    elif i <= afp:
        print("the lake is almost full")
    elif i == f:
        print("the lake is full")
    
    print("Continie?")
    op= int(input("1 = yes \n2 = no \n>"))
    if op == 1:
        continue
    elif op == 2:
        break
    else:
        print("this is not an option")  
        break

