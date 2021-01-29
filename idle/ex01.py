import math
def soma(n):
     '''essa função retorna a soma das fatoriais de um numero n '''
     ''' ->float '''
     somas = 0
     for i in range(n+1):
         somas += ((-1)**i)/(2*i+1)
     return somas

def erro():
    numero = 0
    while not math.fabs(soma(numero)-(math.pi)/4)<0.01:
        numero+1
    return (numero, soma(numero))

print(soma(10))