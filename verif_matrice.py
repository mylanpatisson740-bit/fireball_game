"""
def verif_matrice(L):
    n=len(L)
    for k in range(1,n):
        if len(L[k])!= len(L[0]):
            return False
    return True


print(verif_matrice([[1,2],[3,4],[5]]))
print(verif_matrice([[1,2],[3,4],[5,6]]))
print(verif_matrice([[1,2,3],[4,5,6]]))    
print(verif_matrice([[1],[2,3],[4,5]]))
"""
def matrice_nulle(n,p):
    m=[]
    for i in range(0,n):
        m.append([])
        for j in range(0,p):
            m[i].append(0)
    return m

"""
def addition(a,b):
    if len(a) != len(b)or len(a[0])!= len(b[0]):
        return "on peut pas additionner"
    c=matrice_nulle(len(a),len((a[o])))
    for i in range (0,len(a)):
        for j in range (0,len(a[0])):
            c[i][j]= a[i][j]+b[i][j]
    return c
print(addition([[1,2],[3,4]],[[5,6]]))
"""
def multiplication(A,B):
    if len(A[0]) != len(B) :
        return "la multiplication est impossible"
    C=matrice_nulle(len(A),len(B[0]))
    for i in range (0,len(A)):
        for j in range (0,len(B[0])):
            C[i][j]=0
            for k in range (0,len(A[0])):
                C[i][j] = C[i][j]+ A[i][k]*B[k][j]
    return C
A=[[1,2],[3,4]]
B=[[3,7,6],[5,8,0]]
#print(multiplication(A,B))

def puissance(A,n):
    C=A
    for k in range (2,n+1):
        C=multiplication(C,A)
    return C
A=[[0,1,1,1,0,0],[1,0,0,0,0,1],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,1],[0,0,1,0,0,0]]
print(puissance(A,10))

