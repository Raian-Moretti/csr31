
def manchester_encode(mensagem):
  binario = ""
  for x in mensagem:
    binario += '{0:08b}'.format(ord(x))

  toCompareBinary = ""
  
  cont = 0
  for i in binario:
    
    if(cont == 0):
      if(binario == '0'):
        toCompareBinary += '0'
        cont += 1
        toCompareBinary += '1'
        cont += 1
        continue
      else:
        toCompareBinary += '0'
        cont += 1
        toCompareBinary += '0'
        cont += 1
        continue
    if (i == '0' and toCompareBinary[cont-1] == '0') or (i == '1' and toCompareBinary[cont-1] == '0'):
      toCompareBinary += '1'
    else:
      toCompareBinary += '0'
    cont = cont + 1
    if (i == '0' and toCompareBinary[cont-1] == '1') or (i == '1' and toCompareBinary[cont-1] == '0'):
      toCompareBinary += '0'
    else:
      toCompareBinary += '1'
    cont = cont + 1

  return toCompareBinary

def manchester_decode(manchester):
  decmanchester = ""
  for num in range(1, len(manchester)):
    if(num % 2):
      decmanchester += manchester[num]
  
  return decmanchester
    
def bitstring_to_bytes(s):
  v = int(s, 2)
  b = bytearray()
  while v:
    b.append(v & 0xff)
    v >>= 8
  return bytes(b[::-1])