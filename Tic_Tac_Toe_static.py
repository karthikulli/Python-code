r1=input().split()
r2=input().split()
r3=input().split()
r="Tie"
for col in range(len(r1)):
    if r1[col]=='O' and r2[col]=='O' and r3[col]=='O' :
        r="Abhinav Wins"
        break
    elif r1[col]=='X' and r2[col]=='X' and r3[col]=='X' :
        r="Anjali Wins"
        break
    elif r1[0]=='O' and r1[1]=='O' and r1[2]=='O' :
        r="Abhinav Wins"
        break
    elif r2[0]=='O' and r2[1]=='O' and r2[2]=='O' :
        r="Abhinav Wins"
        break
    elif r3[0]=='O' and r3[1]=='O' and r3[2]=='O' :
        r="Abhinav Wins"
        break
    elif r1[0]=='X' and r1[1]=='X' and r1[2]=='X' :
        r="Anjali Wins"
        break
    elif r2[0]=='X' and r2[1]=='X' and r2[2]=='X' :
        r="Anjali Wins"
        break
    elif r3[0]=='X' and r3[1]=='X' and r3[2]=='X' :
        r="Anjali Wins"
        break
for row in range(3):
    for col in range(3):
        if r=="Abhinav Wins" or r=="Anjali Wins":
            break
        else:
            if row==col :
                if r1[0]=='O' and r2[1]=='O' and r3[2]=='O' :
                    r="Abhinav Wins"
                elif r1[0]=='X' and r2[1]=='X' and r3[2]=='X' :
                    r="Anjali Wins" 
            elif row+col==2:
                if r1[2]=='O' and r2[1]=='O' and r3[0]=='O' :
                    r="Abhinav Wins"
                elif r1[2]=='X' and r2[1]=='X' and r3[0]=='X' :
                    r="Anjali Wins"
    print(r)
    break
