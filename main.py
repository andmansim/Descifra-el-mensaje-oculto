
def abclave(original, preguntita):
  abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  zyx = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
  resultado = ''
  
  if preguntita == 'c':
    abc = abc
    zyx = zyx
  else:
    abc = zyx
    zyx = abc
    
  for i in original:
    resultado += zyx[abc.index(i)]
  return resultado



if __name__ == '__main__':
  preguntita = input('Quieres cifrar o descifrar? (c/d): ')
  original = input("Introduzca la clave: ")
  original = original.upper()
  resultado = abclave(original, preguntita)
  print(resultado)

'GSVUOZTRHHZBDVZIVXIZAB'
'Resultado es: THEFLAGISSAYWEARECRAZY'