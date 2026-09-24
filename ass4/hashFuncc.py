import hashlib

# md5 encryption 
encrypmd5 = hashlib.md5()

encrypmd5.update("Vande Mataram".encode('utf-8'))
hex_digest = encrypmd5.hexdigest()

print(hex_digest)

# sha encryption 
encrypsha1 = hashlib.sha1()

encrypsha1.update("Jai Hind".encode('utf-8'))
hex_digest1 = encrypsha1.hexdigest()

print(hex_digest1)

