def rot13_encrypt(string):
    text = string
    rot13_text = "".join([abc[(abc.find(c)+13)%26] for i in text])
    print(rot13_text)
