def url_verschluesseln():
    print("\n")
    print("URL Verschlüsseln")
    print("\n")
    print("[1] URL verschlüsseln")
    print("[2] URL entschlüsseln")
    print("\n")
    eingabe = input("> ")
    if int(eingabe) == 1:
        print("\n")
        print("URL verschlüsseln")
        print("\n")
        eingabe = input("URL: ")
        def url_verschluesseln(url):
            alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphabet_verschluesselt = "cbaefdjlkihgprqonmzyxwvutsCBAEFDJLKIHGPRQONMZYXWVUTS"
            umwandlung = dict(zip(alphabet, alphabet_verschluesselt))
            return ''.join(umwandlung.get(char, char) for char in url)
        print("Die verschlüsselte URL ist: " + url_verschluesseln(eingabe))
    elif int(eingabe) == 2:
        print("\n")
        print("URL entschlüsseln")
        print("\n")
        eingabe = input("URL: ")
        def url_entschluesseln(url):
            alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphabet_verschluesselt = "cbaefdjlkihgprqonmzyxwvutsCBAEFDJLKIHGPRQONMZYXWVUTS"
            umwandlung = dict(zip(alphabet_verschluesselt, alphabet))
            return ''.join(umwandlung.get(char, char) for char in rot13_url)
        print("Die URL ist: " + url_entschluesseln(eingabe))
