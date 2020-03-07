def sha128_encrypt(string):
    text = string
    h = hashlib.new('ripemd160')
    h.update(text)
    return h.hexdigest()
