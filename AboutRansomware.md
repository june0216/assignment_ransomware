## 랜섬웨어

*가장 일반적인 랜섬웨어(워너크라이의 스크린) - 비트코인으로 보내라  

o 랜섬웨어
• 랜섬웨어는 피해자가 랜섬을 지불하지 않으면 피해자의 데이터를 대중에
공개하거나 아니면 영구적으로 피해자가 접근할 수 없도록 막아버리겠다고
위협하는 공격을 의미함.

*대부분의 피해자들은 금액을 지불하지 않음(데이터가 금액을 지불해도 복호화 안했을 수 있기 때문이다,또한 데이터를 공격자가 가지고 있어서 데이터를 지웠을 수도 있기 때문이다. )그래서 
• 최신 랜섬웨어는 cryptoviral extortion (by Young and Yung, IEEE S&P, 1996) 이라 불리우는 발달된 형태의 공격을 이용함. 이 공격에서는 랜섬웨어는 피해자의 파일을 암호화하여 접근 할 수 없도록 한 후, 이를 복호화 하기 위해서 랜섬을 지불하라고 요구함. 그래서 데이터를 복호화할 때 키가 필요한데 데이터의 키(이렇게 한다면 돈을 지불한다 왜냐하면 공격자가 나의 데이터를 가지고 있지 않고 아직 유출되지 않았다는 것을 알기 때문에 금액을 지불할 수있다.)

• 제대로 구현된 cryptoviral extortion attack, 암호화된 파일을 복호화 키 없이 복구하는 방법은 불가능함. 그리고 랜섬 지불에 사용되는 digital currencies를 추적하는 것도 매우 어려움. (이전에는 계좌를 추적하는 것이 가능하다. 하지만 코인이 발달되면서 추적할 수 없어서 발달되었따

따라서 공격자를 추적하고 법적
제재를 하는 것이 매우 어려워 짐

o **CryptoLocker (2013)**
• 2048 RSA-bit key를 사용함. (이론적으로 감염 이후에 private key (sk) 없이 파일의 encryption key (대칭키)를 복구하는 것은 불가능함.)
• 공격 대상 파일은 특정한 Extension을 가짐.
• 감염 이후, 3일 안에 Bitcoin이나 cash voucher로 랜섬을 지불하도록 요구함.
• Gameover Zeus botnet과 이메일 첨부파일을 통해 확산되었으며, 약 $3 million 의 피해가 보고되었음.
• Gamenover Zeus botnet이 Operation Tovar에 의해 차단되면서 확산이 멈추었음(피해가 차단되었다)

**o WannaCry (2017)**

• **EternalBlue** exploit을 통해 확산됨. EternalBlue exploit NSA에 의해 개발되었으며 Windows의 SMB protocol 취약점을 이용함.

*NSA = 미국의 정보기관

*패치가 만들어졌는데 아직 패치가 되지 않은 컴퓨터들이 wannacry에 감염되었다. 

• 전세계적으로 230,000 여 개의 기기를 감염 시켰으며 여기에는 the British National Health Service (NHS), FedEx, Deutsche Bahn and Honda 등도 주요 시설 및 기업이 포함됨. → 환자의 정보가 없어서 생명피해가 있었다. 

• 북한 해킹 그룹에 의해 개발된 것으로 알려짐.

**o Garmin (2020)**

• Garmin은 GPS **smartwatches 및 wearables 기기에 세계적으로 대표적인 회사**임. 

• wearable devices의 제조사로 자체 데이터 센터에 사용자의 private data (runs and bike rides)를 보유하고 있음..

• 2020 후반, Garmin은 ransomware 공격을 받았고, 이로 인해 제공하는 서비스에 장애를 일으킴.
([https://techbeacon.com/security/8-lessons-garminransomware-attack](https://techbeacon.com/security/8-lessons-garminransomware-attack)).

• Garmin이 얼마의 랜섬을 지불했는 지 정확히 확인되지는 않았지만 데이터의 복호화 키를 얻기 위해 수십억원을 지불한 것으로 알려짐.

*Best Practice는 몸값을 지불하지 않는 것이다. → 랜섬웨어 시장이 커지게 된다. 

### **Hybrid encryption**

랜섬웨어의기본 원리 

• Hybrid encryption은 대칭키 (symmetric key) 암호 알고리즘을 사용하여 메시지를 암호화 하고, 암호화에 사용된 대칭키 (symmetric key) 를 공개키 암호알고리즘의 공개키 (public key)를 이용하여 를
암호화 함.

*공개키로 암호화하면 오래걸리기 때문에(몇년이 걸릴 수있다) 대칭키로 메시지를 암호화하고 공개키로 이 키를 암호화한다. 

• *대칭키를 암호화한 암호문과 메시지를 암호화한 암호문*을 모두 Receiver에게 전달함. 공개키에 매칭되는 비밀키를 가진 Receiver는 이를 복호화 할 수 있음. 

• **대용량의 데이터**를 암호화하기 위한 방법으로 사용됨.

*대칭키로 암호화할 수 있지만 키관리가 어려워서, 키 관리를 주고 받는 것이 어렵다. , 또한 공개키는 너무 오래걸리기 때문에 하이브리드로 사용

o Hybrid encryption - Diagram

![화면 캡처 2022-11-14 101536.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c5d344fb-ced3-438a-8c75-49904f7f072e/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2022-11-14_101536.png)

랜섬웨어의 동작 원리
o 랜섬웨어는 공격자 (Attacker) 와 피해자 (Victim) 사이의
three-round protocol을 통해 수행된다.

(랜섬웨어가 사용자의 컴퓨터에 malware의 형태로 들어간다) 

public키를 포함한 malware를 설치하게ㅚ나. 
• Step 1: 공격자는 공개키와 개인키 키 쌍 (pk, sk) 을 생성하고, 공개키
및 이를 이용한 암호화 프로그램을 Malware에 포함하여 피해자에게
전달한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1e0b008-6d8a-4f4b-b191-03d471b854f5/Untitled.png)

Step 2: 공격을 수행하기 위해, Malware는 랜덤하게 대칭키 k를
생성하고, 피해자의 데이터를 암호화하여 CM을 생성한다. 이후에 대칭키
및 원본 데이터를 삭제하여 데이터가 복구되는 것을 막는다. 이후, 어떻게
ransom을 지불할지에 대한 안내를 피해자의 화면에 출력한다. 피해자는
ransom과 함께 대칭키를 암호한 Ck(키에 대한 암호화) 를 공격자에게 전달한다

*퍼블릭키를 통해서 암호화하는 것이 아니라 랜덤하게 키를 생성하여 메시지를 암호화하고 메시지에 대한 암호문이 생성이 되고 

사용자 컴터에는 평문도 없고 평문키가 없고 단지 암호화된 키와 평문을 암호화한 암호문만 존재한다. 

Ck를 공격자에게 보내라고 한다. CM은 필요없음 k만 알면 CM을 복호화할 수있기 때문이다. 

파일과 몸값을 보내면 복호화할 수있는 키를 주겠다고 함

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9ceb7250-6dce-42f7-bb3d-9afa80ef66d8/Untitled.png)

- Step 3: 공격자가 ransom을 수령한 경우, 공격자는 Ck 를 자신의
비밀키 sk로 복호화 하고, 이에 대한 결과물인 대칭키 k를 피해자에게
보낸다.
    - 피해자는 수령한 대칭키를 이용하여 CM을 k로 복호화 하여
    원본데이터를 복구한다.
    
    ![화면 캡처 2022-11-14 102033.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a14aec74-fa8c-4f2b-b62c-e941db8052ec/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2022-11-14_102033.png)
    
    o 동작 원리에 대한 부가 설명:
    • 랜덤하게 생성된 128-bit 대칭키를 이용한 AES 등의 대칭키 암호
    알고리즘은 매우 안전한 알고리즘으로 정확한 키없이 암호화된 데이터를
    복호화하는 것은 매우 어렵다.
    
    *AES는 제일 안전한 암호화이다. 키없이 복호화 할 수 없다. 
    • 공격자의 개인키는 피해자에게 유출되지 않아도 된다.
    
    *sk를 가지고 사용자의 Ck에 대해 복호화 할 수 있다. 
    
    하나의 퍼블릭키를 두고 랜섬웨어를 반복해도 상관없다. 다른 회사가 다른 사람들과 공유할 수 없다. sk를 알 수없다 (여러 피해자에게 공격자의 개인키인 sk를 공유할 수 없기 때문에 ㅔ(줄 일이 없기) 여러 피해자에게 하나의 sk로 랜섬웨어 제작 가능)
    • 피해자는 오직 아주 작은 크기의 암호문 Ck
    (대칭키가 암호화된
    암호문)을 공격자에게 전달하면 되기에 ransom을 지불하는 과정이
    효율적이며 단순하다.
    
    o hybrid encryption과의 관계
    • 기본적으로 **데이터 암호화를 공개키 암호화로부터 분리한다는 측면**에서
    공격이 더 효율적으로 이루어지며 이는 hybrid encryption과 같은
    원리이다.
