
def alfa (numero):
    resultado=0
    for j in range (1,5):
        resultado+= numero+2
    final = beta(resultado)
    return final

def beta (numero):
    return  numero/2.0

print(alfa(2))

    