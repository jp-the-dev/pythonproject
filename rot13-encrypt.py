def rot13_encrypt(string):
    text = string
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot13_text = "".join([alphabet[(alphabet.find(c)+13)%26] for i in text])
    print(rot13_text)
