import hashlib


def sha512_encrypt(string):
  sha_signatur = \
  hashlib.sha256(string.encode()).hexdigest()
  return sha_signatur
  
