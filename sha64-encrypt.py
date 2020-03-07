import hashlib


def sha64_encrypt(string):
  sha_signatur = \
  hashlib.sha64(string.encode()).hexdigest()
  return sha_signatur
