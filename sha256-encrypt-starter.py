sha256_encrypt = __import__('sha256-encrypt')
eingabe = input("String: ")
string = eingabe
print(sha256_encrypt.sha256_encrypt(string))
