"""
def truc(n):
    if n%2==0:
        return True
    else:
        return False
print(truc(13))
print()
"""
""" meme partité"""
"""
def machin(a):
    b="debut"
    for k in range(4,9):
        if a%2==0:
            b=b+"e"
        else:
            b="fin"
        a=a+k
    return(b)
print(machin(5))
print()
"""

def lol(v,f):
    if v%2==0 and f%2==0:
        return True
    elif v%2==1 and f%2==1:
            return True
    else:
        return False
print(lol(7,6))
print()
"""""
cpt=0
b=1
c=2
for a in range(1,101):
    atemp = a
    if lol(a,b):
        a=2*a
        b=2*a+1
    if lol(a,c):
         a=3*a
         c=3*a+1
    if c==atemp+1:
        cpt=cpt+1
        print("pour",atemp,"ca marche")
print(cpt)
"""""""""""
def test(p):
    a=True
    for k in range(1,len(str(p))):
        if p% int(str(p)[k]) !=0:
            a=False
    return(a)
print(test(31218))

    
