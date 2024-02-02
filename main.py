
def abclave(original, preguntita):
  abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  zyx = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
  resultado = ''
  
  if preguntita == 'c':
    abcz = abc
    zyxa = zyx
  else:
    abcz = zyx
    zyxa = abc
    
  for i in original:
    resultado += zyxa[abcz.index(i)]
  return resultado



if __name__ == '__main__':
  preguntita = input('Quieres cifrar o descifrar? (c/d): ')
  original = input("Introduzca la clave: ")
  original = original.upper()
  resultado = abclave(original, preguntita)
  print(resultado)

'GSVUOZTRHHZBDVZIVXIZAB'
'Resultado es: THEFLAGISSAYWEARECRAZY'