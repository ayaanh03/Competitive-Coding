
n,k=map(int,input().split())
m = [[-1]*n]*n

def R(a,b):
    m[a],m[b]=m[b],m[a]

def C(a,b):
    l = n
    if l%2 == 0:
        for i in range(l//2):
            m[i][a],m[i][b]=m[i][b],m[i][a]
            m[l-i-1][a],m[l-1-i][b]=m[l-1-i][b],m[l-1-i][a]
    else:
        for i in range(l//2):
            m[i][a],m[i][b]=m[i][b],m[i][a]
            m[l-i-1][a],m[l-1-i][b]=m[l-1-i][b],m[l-1-i][a]
        i = l//2
        m[i][a],m[i][b]=m[i][b],m[i][a]

def A(a,b):
    print(m[a][b])
for i in range(n):
    m[i] = list(map(int,(input().split())))

for i in range(k):
    i,a,b = input().split()
    if i=='A':
        A(int(a)-1,int(b)-1)
    if i=='R':
        R(int(a)-1,int(b)-1)
    if i=='C':
        C(int(a)-1,int(b)-1)
