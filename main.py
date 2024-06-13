import random
def det(matris, raw, col):
    #detA=a21*A21+a22*A22+a23*A23
    choose=1
    det=0
    if raw == 1 and col == 1:
        return matris[0][0]
    if raw == 2 and col == 2:
        return int(matris[0][0]) * int(matris[1][1]) - int(matris[0][1]) * int(matris[1][0])
    else:
        for j in range(0,col):
        
            det=det+int(matris[choose][j])*int(cof(matris,choose,j,raw,col))
        return det
def cof(matris,raw, col,maxraw, maxcol):
    new_matris=[]
    if maxcol==0:
        a=matris[0][0]
        return a
    for i in range(0,maxraw):
        if i==raw:
            continue
        new_row=[]
        for j in range(0,maxcol):
            if j==col:
                continue
            new_row.append(matris[i][j])
        new_matris.append(new_row)
    
    a=(-1)**(raw+col)*det(new_matris,maxraw-1,maxcol-1)
    return int(a)


matris=[]
raw=int(input("Satır:"))
col=int(input("Sütun:"))
for i in range(0,raw):
    matris.append([])
    for j in range(0,col):
        num=input(f"{i+1}.satırın {j+1}. elemanını girin:")
        matris[i].append(num)
print(f"Determinant: {det(matris,raw,col)}")
