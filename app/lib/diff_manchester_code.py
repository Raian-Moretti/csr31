import re
def diff_manchester_encode(mensagem):
  binario = ""
  for x in mensagem:
    binario += '{0:08b}'.format(ord(x))

  toCompareBinary = ""
  
  cont = 0
  for i in binario:
    if(cont == 0):
      if(i == '0'):
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

def diff_manchester_decode(manchester):
  decmanchester = ""
  twoBits = re.findall("..", manchester)
  for x in range(len(twoBits)):
    if x == 0:
      if twoBits[x] == '00':
        decmanchester+= '0'
      if twoBits[x] == '01':
        decmanchester+= '0'
      if twoBits[x] == '10':
        decmanchester+= '0'
      if twoBits[x] == '11':
        decmanchester+= '1'
      continue  

    if twoBits[x] == '00' and twoBits[x-1][1] == '0':
      decmanchester+= '1'
    if twoBits[x] == '00' and twoBits[x-1][1] == '1':
      decmanchester+= '1'
    if twoBits[x] == '01' and twoBits[x-1][1] == '0':
      decmanchester+= '1'
    if twoBits[x] == '01' and twoBits[x-1][1] == '1':
      decmanchester+= '0'
    if twoBits[x] == '10' and twoBits[x-1][1] == '0':
      decmanchester+= '0'
    if twoBits[x] == '10' and twoBits[x-1][1] == '1':
      decmanchester+= '0'
    if twoBits[x] == '11' and twoBits[x-1][1] == '0':
      decmanchester+= '1'
    if twoBits[x] == '11' and twoBits[x-1][1] == '1':
      decmanchester+= '0'

  return decmanchester
    
def bitstring_to_bytes(s):
  v = int(s, 2)
  b = bytearray()
  while v:
    b.append(v & 0xff)
    v >>= 8
  return bytes(b[::-1])