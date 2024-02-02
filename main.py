
def abclave(original):
  abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  zyx = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
  resultado = ''
  for i in original:
    resultado += zyx[abc.index(i)]
  return resultado


if __name__ == '__main__':
  original = input("Introduzca la clave: ")
  resultado = abclave(original)
  print(resultado)

'GSVUOZTRHHZBDVZIVXIZAB'
'Resultado es: THEFLAGISSAYWEARECRAZY'