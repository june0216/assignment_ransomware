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
from base64 import b64decode
from Crypto.Util.py3compat import *

from Crypto.Cipher import PKCS1_OAEP

def decrypt_file(key, in_filename, out_filename=None):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    iv = '0pXvAAg0oqRpVJHm6QgwBQ=='
    iv = b64decode(iv)

    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            data = infile.read(filesize)
            data = b64decode(data)
            pt = unpad(decryptor.decrypt(data), AES.block_size)
            outfile.write(pt)


def main():
    f = open("/home/kali/attacker/key.txt", "rb")
    key = f.read()
    key = b64decode(key)
    f.close()
    startPath = './*.enc'
   

	
#Decrypts the files
    for filename in glob.iglob(startPath, recursive=True):
        if(os.path.isfile(filename)):
            fname, ext = os.path.splitext(filename)
            if (ext == '.enc'):
                decrypt_file(key, filename)
                os.remove(filename)
                print('Decrypting file => ' + filename)

main()
