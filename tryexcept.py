from os import error


""" try:
    with open ('arquitvo.txt', 'r') as arquivo:
        texto = arquivo.read()
        print(texto)

except FileNotFoundError as error:
    print(error)

except:
    print('deu ruim') """

a = 10
b = 2
try:
    print(a/b)
except ZeroDivisionError as error:
    print(error)

else:
   print( 'Sem erros')

finally:
    print(' Aqui sempre vai printar')