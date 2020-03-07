rot13_encrypt = __import__('rot13-encrypt')
eingabe = input("String: ")
string = eingabe
rot13_encrypt.rot13_encrypt(string)
