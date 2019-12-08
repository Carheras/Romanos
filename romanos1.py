valores = {"I": 1, "V": 5, "X":10 , "L":50 , "C": 100, "D": 500, "M": 1000}
valores5 = {"V": 5 , "L":50 , "D":500}
simbolos = ["I", "V", "X", "L", "C", "D", "M"]

#DICCIONARIOS:

unidades = {1: "I", 5: "V", "next": "X"}
decenas = {1: "X" , 5: "L" , "next": "C"}
centenas = {1: "C" , 5: "D" , "next": "M"}
millares = {1: "M" , "next": ""}

rangos = {0 : unidades , 1 : decenas, 2 : centenas , 3 : millares}

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

def invertir(cadena):
    res = ""
    for i in range(len(cadena)-1 , -1 , -1):
            res+= cadena[i]
    return res

def aRomano(numero):
    cad = invertir(str(numero))
    result = ""
    for i in range(len(cad)):
        digit = int(cad[i])
        if digit <= 3:
            result+= digit*rangos[i][1]
        elif digit == 4:
            result+= digit*rangos[i][5]
        elif digit == 5:
            result+= rangos[i][5]
        elif digit < 9:
            result+= (rangos[i][5]+rangos[i][1]*(digit-5))
        else:
            result+= rangos[i][1]+rangos[i]["next"]
    return invertir(result)




print(aRomano(1830))


