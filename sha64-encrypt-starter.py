sha64_encrypt = __import__('sha64-encrypt')
eingabe = input("String: ")
string = eingabe
print(sha64_encrypt.sha64_encrypt(string))
