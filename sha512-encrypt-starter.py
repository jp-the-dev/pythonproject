sha512_encrypt = __import__('sha512-encrypt')
eingabe = input("String: ")
string = eingabe
print(sha512_encrypt.sha512_encrypt(string))
