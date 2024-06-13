def det(matris, row, col):
    #detA=a21*A21+a22*A22+a23*A23
    choose=1
    det=0
    if row == 1 and col == 1:
        return matris[0][0]
    if row == 2 and col == 2:
        return int(matris[0][0]) * int(matris[1][1]) - int(matris[0][1]) * int(matris[1][0])
    else:
        for j in range(0,col):
        
            det=det+int(matris[choose][j])*int(cof(matris,choose,j,row,col))
        return det
def cof(matris,row, col,maxrow, maxcol):
    new_matris=[]
    if maxcol==0:
        a=matris[0][0]
        return a
    for i in range(0,maxrow):
        if i==row:
            continue
        new_row=[]
        for j in range(0,maxcol):
            if j==col:
                continue
            new_row.append(matris[i][j])
        new_matris.append(new_row)
    
    a=(-1)**(row+col)*det(new_matris,maxrow-1,maxcol-1)
    return int(a)


matris=[]
row=int(input("Satır:"))
col=int(input("Sütun:"))
for i in range(0,row):
    matris.append([])
    for j in range(0,col):
        num=input(f"{i+1}.satırın {j+1}. elemanını girin:")
        matris[i].append(num)
print(f"Determinant: {det(matris,row,col)}")

