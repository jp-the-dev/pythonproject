import hashlib


def sha128_encrypt(string):
  sha_signatur = \
  hashlib.sha128(string.encode()).hexdigest()
  print(sha_signatur)
