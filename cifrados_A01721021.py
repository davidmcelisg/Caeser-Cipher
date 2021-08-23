"""
Autor: David Martínez Celis
Emial: a01721021@itesm.mx
Instrucciones: Haz un programa el cual haga cifrado cesareo
"""
"""
-%Run cifrados_A01721021.py
Dame palabra a cifrar: avatar
dame shift/llave (entre 0 y 25): 25
Su mensaje cifrado es:  zuzszq
Su mensaje descifrado es:  avatar
-%Run cifrados_A01721021.py
Dame palabra a cifrar: David
dame shift/llave (entre 0 y 25): 20
Su mensaje cifrado es:  xupcx
Su mensaje descifrado es:  david
-%Run cifrados_A01721021.py
Dame palabra a cifrar: mensajedeprueba
dame shift/llave (entre 0 y 25): 30
Valor invalido, shift/llave tiene que ser número entre 0 y 25
"""
mensaje = input("Dame palabra a cifrar: ").lower()
shift = input("dame shift/llave (entre 0 y 25): ")
#listas para cifrar/descifrar las letras
intermedio_cifrado =[]
intermedio_descifrado =[]
encriptado = []
decriptado = []
#chequeo de sanidad para shift
def esnumero(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
    
def chequeo(n):
    if esnumero(n) == False:
        print("Valor invalido,  shift/llave tiene que ser número entre 0 y 25")
        exit()
#funciones para aplicar cifrado cesareo usando el número en shift
def cifrado(n):
    if (n + shift) >= 25:
        n = ((n + shift)%25 -1)
        if n == -1:
            n = 25
    else:
        n = (n + shift)%26
    intermedio_cifrado.append(n)

def descifrado(n):
    if (n - shift) < 0:
        n = ((n - shift)%25 + 1)
    else:
        n = (n - shift)%26
    intermedio_descifrado.append(n)
#chequeo de sanidad para variable shift
chequeo(shift)
shift = int(shift)
if shift > 25:
    print("Valor invalido, shift/llave tiene que ser número entre 0 y 25")
    exit()
#diccionario letras a números
letras = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25
    }
#diccionario números a letras
cifrados_reves = {
    "0":"a",
    "1":"b",
    "2":"c",
    "3":"d",
    "4":"e",
    "5":"f",
    "6":"g",
    "7":"h",
    "8":"i",
    "9":"j",
    "10":"k",
    "11":"l",
    "12":"m",
    "13":"n",
    "14":"o",
    "15":"p",
    "16":"q",
    "17":"r",
    "18":"s",
    "19":"t",
    "20":"u",
    "21":"v",
    "22":"w",
    "23":"x",
    "24":"y",
    "25":"z"
    }
#se pasan letras de mensaje a numeros
for y in mensaje:
    if y in letras:
        encriptado.append(letras[y])
#se suma número shift para cifrar
for i in encriptado:
    cifrado(i)
#números se hacen strings para cifrar
inter = []
for i in intermedio_cifrado:
    x = str(i)
    inter.append(x)
#se pasan números cifrados a letras
cesareo = ""
for i in inter:
    x = cifrados_reves[i]
    cesareo = cesareo + x
#se imprimen letras cifrados
print("Su mensaje cifrado es: ", cesareo)
#letras se vuelven a pasar a números
for y in cesareo:
    if y in letras:
        decriptado.append(letras[y])
#se resta su valor de shift para volver a originales/descifrados
for i in decriptado:
    descifrado(i)
#numeros descifrados se hacen strings para cifrar
final = []
for i in intermedio_descifrado:
    x = str(i)
    final.append(x)
#se pasan numeros descifrados a letras originales
cesareo_original = ""
for i in final:
    x = cifrados_reves[i]
    cesareo_original = cesareo_original + x
#se imprimen letras originales/mensaje descifrado
print("Su mensaje descifrado es: ", cesareo_original)