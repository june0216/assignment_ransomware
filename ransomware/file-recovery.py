import glob
import os, random, struct
from Cryptodome.Cipher import AES
import sys
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA
from base64 import b64decode
from Crypto.Util.py3compat import *

from Crypto.Cipher import PKCS1_OAEP

def decrypt_file(key, in_filename, out_filename=None):#파일을 복호화하는 함수이다. 
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]# 파일명이 지정되지 않다면 기존파일의 이름(원래 이름 1.txt.enc에서 1.txt를 추출한다. )
    iv = '0pXvAAg0oqRpVJHm6QgwBQ=='# iv 값을 고정시켰다.(base64형태이다. )
    iv = b64decode(iv)#iv값을 decode하여 실행한다

    filesize = os.path.getsize(in_filename)#파일의 사이즈를 알아온다. 
    with open(in_filename, 'rb') as infile:#파일을 연다. 
        decryptor = AES.new(key, AES.MODE_CBC, iv)# AES로 암호화된 CBC mode을 생성하여 cipher에 저장

        with open(out_filename, 'wb') as outfile:#복호화한 내용을 같은 이름의 txt형태로 저장할 것이다. 
            data = infile.read(filesize)#파일 사이즈만큼 읽고 
            data = b64decode(data)#64로 decode한 다음
            pt = unpad(decryptor.decrypt(data), AES.block_size)#암호화를 위해 패딩하여 저장한 것을 unpad하여 원래의 값을 알아낸다. 
            outfile.write(pt)#파일에 원래의 값 저장한다. 


def main():
    f = open("../attacker/key.txt", "rb")#key.txt를 읽어와 복호화를 진행할 것이다. 
    key = f.read()#key 파일을 읽어온다. 
    key = b64decode(key)#base64형태로 저장되어있기 때문에 decode한 값을 알아낸다. 
    f.close()#파일을 닫는다. 
    startPath = './*.enc'#복호화할 대상은 해당 경로에 있는 .enc 파일이다. 
   

	
#파일들을 복호화한다. 
#glob를 활용하여 동일하게 데이터위치에서 .enc로 끝나는 모든 파일명을 가져올수 있다. 
    for filename in glob.iglob(startPath, recursive=True): #대상 경로를 재귀적으로 호출하여 해당 폴더에 있는 파일들을 다 가지고 온다. 
        if(os.path.isfile(filename)):#파일일 경우
            fname, ext = os.path.splitext(filename)#확장자와 파일 명을 분리한다. 
            if (ext == '.enc'):#확장자가 enc인 것만(암호화된 것만) 복호화를 한다. 
                decrypt_file(key, filename)# 파일을 복호화하는 함수를 호출한다. 
                os.remove(filename)#복호화한 후 파일을 지운다. 
                print('Decrypting file => ' + filename)#복호화한 파일을 하나씩 출력한다. 

main()# main 을 실행한다. 
