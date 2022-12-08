from Crypto.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Crypto.PublicKey import RSA
from base64 import b64encode

file_in = open("/home/kali/victim/key.bin", "rb")
private_key = RSA.import_key(open("/home/kali/attacker/private.pem").read())
enc_data = file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)
data = cipher_rsa.decrypt(enc_data)
file_out = open("/home/kali/attacker/key.txt", "wb")
data = b64encode(data)
file_out.write(data)
file_in.close()
