valores = {"I": 1, "V": 5, "X":10 , "L":50 , "C": 100, "D": 500, "M": 1000}
valores5 = {"V": 5 , "L":50 , "D":500}
simbolos = ["I", "V", "X", "L", "C", "D", "M"]
def aArabigo(numromano):
    numarabigo = 0
    numrepes = 1
    ultimosimbolo = ""
    for letra in numromano:
        if letra in valores:
            numarabigo += valores[letra]
            if ultimosimbolo == "":
                pass
            elif valores[ultimosimbolo] > valores[letra]:
                numrepes = 1
            elif valores[ultimosimbolo] == valores[letra]:
                numrepes += 1
                if letra in valores5:
                    return 0
                if numrepes > 3:
                    return 0
            elif valores[ultimosimbolo] < valores[letra]:
                if (numrepes > 1) or (ultimosimbolo in valores5):
                    return 0
                distancia = simbolos.index(letra) - simbolos.index(ultimosimbolo)
                if distancia > 2:
                    return 0


                numarabigo = (numarabigo-valores[ultimosimbolo]) + (valores[letra]- valores[ultimosimbolo])
                numrepes = 1
        
        else:
            return 0
        ultimosimbolo = letra
        
    return numarabigo

print (aArabigo("VV"))


