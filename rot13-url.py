def rot13_url():
    print("\n")
    print("Rot13 URL")
    print("\n")
    print("[1] Rot13 URL erstellen")
    print("[2] Rot13 URL lesen")
    print("\n")
    eingabe = input("> ")
    if int(eingabe) == 1:
        print("\n")
        print("Rot13 URL erstellen")
        print("\n")
        eingabe = input("URL: ")
        def url_zurot13(url):
            alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphabet_fuerrot13 = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
            umwandlung = dict(zip(alphabet, alphabet_fuerrot13))
            return ''.join(umwandlung.get(char, char) for char in url)
        print("Die Rot13 URL ist: " + url_zurot13(eingabe))
    elif int(eingabe) == 2:
        print("\n")
        print("Rot13 URL lesen")
        print("\n")
        eingabe = input("Rot13 URL: ")
        def rot13_zuurl(rot13_url):
            alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphabet_fuerrot13 = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
            umwandlung = dict(zip(alphabet_fuerrot13, alphabet))
            return ''.join(umwandlung.get(char, char) for char in rot13_url)
        print("Die URL ist: " + rot13_zuurl(eingabe))
