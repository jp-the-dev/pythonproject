def rot13_destroyer(self):
    print("\n")
    print("Rot13-Destroyer")
    print("\n")
    datei = open(self, "r")
    text = datei.read()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot13_text = "".join([alphabet[(alphabet.find(i)+13)%26] for i in text])
    datei.close()
    datei = open(self, "w")
    datei.write(rot13_text)
    datei.close()
