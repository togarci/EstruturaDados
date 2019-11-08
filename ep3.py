matriz = """0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110""".split()

def arvore(x, y, matriz):
    alVerify = []
    for k in range(y, len(matriz[x])):
        if matriz[x][k] == "1": alVerify.append((x,k))   
        else: break
    for k in range(y, -1):
        if matriz[x][k] == "1": alVerify.append((x,k))   
        else: break
    return alVerify
        
arvoreParametrizada = []
def check(a, b):
    if matriz[a][b] == "0":
        return False
    elif len(arvoreParametrizada)>0:
        for i in arvoreParametrizada:
            for z in i:
                if a == z[0] and b == z[1]:
                    return False
            
        return True
    else:
        return True

def checkDown(x, p):
    a = []
    for i in range(len(arvoreParametrizada)):
        if i != p:
            for z in arvoreParametrizada[i]:
                if z[0] == x[0]+1 and z[1] == x[1]:
                    a.append(i)
                    i += 1
    return a

def merge():
    for i in range(0, len(arvoreParametrizada)):
        try:
            for z in arvoreParametrizada[i]:
                a = checkDown(z, i)
                if len(a) > 0:
                    for x in a:
                        arvoreParametrizada[i].extend(arvoreParametrizada[x])
                        arvoreParametrizada.remove(arvoreParametrizada[x])
                
        except:pass

def replace(n, x, y):
    if n == "0": return n
    else:
        cont = 1        
        for i in arvoreParametrizada:
            for z in i:
                if z[0] == x and z[1] == y:
                    return str(cont)
            cont += 1
for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        if check(x, y):
            arvoreParametrizada.append(arvore(x, y, matriz))
    merge()

for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        print(replace(matriz[x][y],x,y),end="")
    print("")
