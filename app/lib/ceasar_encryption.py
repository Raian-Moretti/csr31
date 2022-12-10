class CeasarEncryption:
  def __init__(self, key):
    self.key = key

  def encrypt(self, text):
    b = bytes(text, "utf-8")
    encrypted = []
    for byte in b:
      encrypted.append((byte + self.key) % 255)
    
    return bytes(encrypted)

  def decrypt(self, text):
    b = bytes(text, "utf-8")
    decrypted = []
    for byte in b:
      if (byte - self.key) < 0:
        decrypted.append(byte - self.key + 255)
      else:
        decrypted.append(byte - self.key)
    
    return bytes(decrypted)
