valores = {'I':1, 'V': 5, 'X':10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
valores5 = { 'V': 5,  'L': 50,  'D': 500 } 
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

#DICCIONARIOS:

unidades = {1: "I", 5: "V", "next" : X}
decenas = {1 : X, 5 : "L" , "next" : "C"}
centenas = {1 : "C" , 5 : "D" , "next" : "M"}
millares = {1 : "M" , "next" : ""}

rangos = {0 : unidades , 1 : decenas, 3 : centenas , 4 : millares}


def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''
    for letra in numRomano: 
        #incrementamos el valor del número arábigo con el valor numérico del símbolo romano
        if letra in valores:
            numArabigo += valores[letra]
            if ultimoCaracter == '':
                pass
            elif valores[ultimoCaracter] > valores[letra]:
                numRepes = 1
            elif valores[ultimoCaracter] == valores[letra]:
                numRepes += 1
                if letra in valores5:
                    return 0

                if numRepes > 3:
                    return 0


            elif valores[ultimoCaracter] < valores[letra]:
                if numRepes > 1: # No permite repeticiones en las restas
                    return 0

                if ultimoCaracter in valores5: #No permite restas de valores de 5 (5, 50, 500)
                    return 0

                distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter) #No permite que se resten unidades de más de un orden
                if distancia > 2:
                    return 0

                numArabigo -= valores[ultimoCaracter]*2
                numRepes = 1
        else:  #si el simbolo romano no es permitido devolvemos error (0)
            return 0

        ultimoCaracter = letra

    return numArabigo
def invertir(cad):
    res = ""
    for i in range(len(cad)-1 , -1 , -1):
            res+= cad [i]
            
def arabigo_a_romano(valor):
    cad = inviertir(str(valor)

    for i in range (len(cad)):
        digit = int(cad[i])
        if digit <= 3:
            digit*rangos[i][1]
        elif digit <= 4:
            digit*rangos


    


    1.- Descomponer valor en dígitos separando millares, centenas, decenas y unidades
    2.- Procesar uno a uno estos dígitos y transformarlos en su forma romana 
    3.- Ir concatenando cada resultado en una cadena completa
    4.- Devolverla