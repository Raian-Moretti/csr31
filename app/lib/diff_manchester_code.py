import re
def diff_manchester_encode(message):
  binary = ""
  for x in message:
    binary += '{0:08b}'.format(ord(x))

  toCompareBinary = ""
  
  clock = 0
  for i in binary:
    if(clock == 0):
      if(i == '0'):
        toCompareBinary += '0'
        clock += 1
        toCompareBinary += '1'
        clock += 1
        continue
      else:
        toCompareBinary += '0'
        clock += 1
        toCompareBinary += '0'
        clock += 1
        continue
    if (i == '0' and toCompareBinary[clock-1] == '0') or (i == '1' and toCompareBinary[clock-1] == '0'):
      toCompareBinary += '1'
    else:
      toCompareBinary += '0'
    clock = clock + 1
    if (i == '0' and toCompareBinary[clock-1] == '1') or (i == '1' and toCompareBinary[clock-1] == '0'):
      toCompareBinary += '0'
    else:
      toCompareBinary += '1'
    clock = clock + 1

  return toCompareBinary

def diff_manchester_decode(manchester):
  decoded_manchester = ""
  twoBits = re.findall("..", manchester)
  for x in range(len(twoBits)):
    if x == 0:
      if twoBits[x] == '00':
        decoded_manchester+= '0'
      if twoBits[x] == '01':
        decoded_manchester+= '0'
      if twoBits[x] == '10':
        decoded_manchester+= '0'
      if twoBits[x] == '11':
        decoded_manchester+= '1'
      continue  

    if twoBits[x] == '00' and twoBits[x-1][1] == '0':
      decoded_manchester+= '1'
    if twoBits[x] == '00' and twoBits[x-1][1] == '1':
      decoded_manchester+= '1'
    if twoBits[x] == '01' and twoBits[x-1][1] == '0':
      decoded_manchester+= '1'
    if twoBits[x] == '01' and twoBits[x-1][1] == '1':
      decoded_manchester+= '0'
    if twoBits[x] == '10' and twoBits[x-1][1] == '0':
      decoded_manchester+= '0'
    if twoBits[x] == '10' and twoBits[x-1][1] == '1':
      decoded_manchester+= '0'
    if twoBits[x] == '11' and twoBits[x-1][1] == '0':
      decoded_manchester+= '1'
    if twoBits[x] == '11' and twoBits[x-1][1] == '1':
      decoded_manchester+= '0'

  return decoded_manchester
    
def string_to_byte(s):
  v = int(s, 2)
  b = bytearray()
  while v:
    b.append(v & 0xff)
    v >>= 8
  return bytes(b[::-1])