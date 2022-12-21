# study_Attack
먼저, 과제2의 전반적인 수행 과정 및 결과를 살펴보고 이후 랜섬웨어코드에 대해서 구체적으로 살펴볼 것이다. 

먼저, 과제2를 수행하기 위한 과정은 다음과 같다. 

피해자의 컴퓨터 환경은 python3.5 이상인 파이썬과 pycrytodome 패키지가 설치되어있다는 가정이 있었다. 

### A. 과제 작성 과정

**(1) 폴더 생성**

- 먼저, 피해자 컴퓨터를 의미하는 “victim”폴더와 공격자 컴퓨터를 의미하는 “attacker”폴더를 생성한다.
- 전제 = 이 두 개의 폴더는 같은 위치에 있다는 것을 가정하여 작성했다.

**(2) txt 파일 생성**

- “victim”폴더에 다음과 같은 **`txt파일`**을 저장한다. **`1.txt`**, **`2.txt`**, **`3.txt`**을 저장한다.

**(3) “ransom.py”파일을 작성**

그리고 피해자의 컴퓨터에는 이미 랜섬웨어 프로그램이 설치되어있다고 가정했으므로 이 폴더에 랜섬웨어 프로그램인 **`ransom.py`**파일을 작성하여 저장한다. 

이때, **`ransom.py`**에는 

- 파일을 AES_CBC 암호화를 위한 128비트 대칭키를 랜덤 생성
- 이를 가지고 랜섬웨어가 있는 폴더에 모든 `**.txt 파일**`들을 **`.enc파일`**로 암호화
- 암호화가 다 완료되면 **`.txt파일`**들은 모두 삭제하고 *“Your files are encryted. To decryt them, you need to pay me $5000 and send key.bin in your folder to ziyun1612@ewhain.net”*을 터미널에 출력한다.
- 앞에서 생성한 대칭키를 RSA를 사용하여 암호화하여 **`key.bin`**에 저장한다.
    - 이때, key.bin은 피해자의 컴퓨터에 있어야 피해자가 돈과 함께 key.bin을 보내주고 복호화해줄 수 있다. 그래서 피해자의 컴퓨터를 의미하는 victim 폴더내에 key.bin을 저장한다.
    - 한편, RSA는 공개키 암호 알고리즘 중 하나이며 두 개의 키를 사용하는데 모두에게 공개하는 receiver key(공개키)와 공개해서는 안 되는 private key있다.
        - 공격자가 RSA를 통해 키를 암호화하고 여기서 나온 개인키를 가진다. 그리고 피해자에게는 receiver key(공개키)를 가지고 있게 하여 위에서 사용된 대칭키를 이 공개키로 암호화하게 한다. 나중에 **`key.bin`**을 공격자가 자신이 가진 private key로 복호화하여 **`key.bin`**의 내용을 알 수 있게 된다.
    

**(4) key - recovery 프로그램을 만든다.** 

- **`ransom.py`**에서 사용된 key를 암호화한 **`key.bin`**을 받아서 이를 복호화한다.
- 그리고 base64의 형태로 **`key.txt`**에 저장한다.
- 이 프로그램은 공격자가 가지고 있어야 하므로 attacker 폴더에 저장한다.

**(5) file -recovery 프로그램을 만든다.** 

- 암호화된 파일을 복호화하기 위한 파일이다.
- 이 프로그램은 피해자의 컴퓨터에 있어야 피해자가 암호화된 파일을 복호화할 수 있으므로 피해자의 컴퓨터를 의미하는 “victim”폴더에 저장한다.
- 이 폴더 내에 암호화된 **`.enc파일`** 을 가지고 key-recovery 프로그램을 통해 복호화한 **`key.txt`**를 이용하여 파일을 복호화한다.
- 과제에 조건에 없었지만 랜섬웨어와 비슷하게 동작하기 위해 암호화된 파일을 지워주고 복호화된 파일만 남도록 했다.

### B. 프로그램 단계별 실행 화면

**(1) 처음 세팅**

**[처음 victim 폴더]**

![실행전피해자파일.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f274593a-6b54-4f80-a94d-ea4d2e432805/%EC%8B%A4%ED%96%89%EC%A0%84%ED%94%BC%ED%95%B4%EC%9E%90%ED%8C%8C%EC%9D%BC.png)

**[처음 attacker의 폴더]**

![key-recovery위치.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68d1eeb1-69ab-4d85-9313-fd75fc8abf2a/key-recovery%EC%9C%84%EC%B9%98.png)

- **랜섬웨어 전체 동작**

![공격과정.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4f75234-6eb3-4391-9caa-7f092f2df267/%EA%B3%B5%EA%B2%A9%EA%B3%BC%EC%A0%95.png)

이제 명령어 별로 자세히 동작 과정을 살펴볼 수 있다. 

(2) 먼저 victim 폴더 (피해자 컴퓨터)에 있는 랜섬웨어 프로그램(ransom.py)을 실행한다

- [명령어]

```bash
cd victim 
python3 ransom.py
```

[`**ransom.py**`](http://ransom.py) 안에 key를 RSA 암호화 알고리즘을 이용하여 암호화하는 부분도 있으므로 공개키인 **`receiver.pem`**과 개인키 **`private.pem`**이 생성되어 공개키는 victim 폴더에 저장되고 개인키는 attacker 폴더에 저장된다. 

그리고 개인키를 통해 key를 암호화하여 victim 폴더에 **`key.bin`**으로 저장된다. 

**[결과 : 이를 수행한 후 victim 폴더]**

![랜섬웨어감염된피해자파일.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f4f88a9a-92c3-4f18-84a8-4afe6ca98d7d/%EB%9E%9C%EC%84%AC%EC%9B%A8%EC%96%B4%EA%B0%90%EC%97%BC%EB%90%9C%ED%94%BC%ED%95%B4%EC%9E%90%ED%8C%8C%EC%9D%BC.png)

**[결과 : 이를 수행한 후 attacker 폴더]**

![랜섬웨어감염된후공격자파일.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e0f3004-23cd-4818-b428-f9c59606461e/%EB%9E%9C%EC%84%AC%EC%9B%A8%EC%96%B4%EA%B0%90%EC%97%BC%EB%90%9C%ED%9B%84%EA%B3%B5%EA%B2%A9%EC%9E%90%ED%8C%8C%EC%9D%BC.png)

(3) key를 복호화하여 key.txt로 저장한다. 

- [명령어]

```bash
cd ../attacker
python3 key-recovery.py
```

먼저 key를 복호화할 수 있는 건 공격자가 해야 하므로 공격자 폴더(attacker 폴더)에 들어간다. 

그리고 key-recovery.py를 실행하여 피해자가 가지고 있는 **`key.bin`**을 복호화하여 attack 폴더(공격자 폴더에 **`key.txt`**로 저장한다. 

이때, key-recovery 과정은 피해자가 돈을 준 후 파일을 복호화하기 위한 과정의 시작이다. 과제에서 암호화 후 보여주는 메시지에서 피해자에게 “돈과 **`key.bin`**을 주면 복호화해주겠다”라고 요구한다.  하지만 실제 랜섬웨어에서는 공격자에게 돈과 **`key.bin`**을 주겠지만 여기서는 그러한 환경이 아니기 때문에 `**key.bin**`을 넘겨주는 과정을 생략한다. 그렇기 때문에 **`key-recovery.py`**에서 직접 피해자 폴더에 접근하여 key.bin을 여는 것으로 대체하였다. 

또한, 복호화 후 `**key.txt**`를 다시 피해자에게 넘겨주어야 하는데 과제 환경상 불가능하다. 그렇기 때문에 직접 공격자가 피해자에게 **`key.txt`**를 전달하는 과정을 생략하고 victim 폴더(피해자)가 가지고 있는 `**file-recovery.py**`에서 attacker폴더에 접근하여 **`key.txt`**로 암호화된 파일을 txt파일로 복호화하는 작업으로 대체하였다. 

**[결과 : key를 복호화한 후 공격자의 폴더(attacker)]**

**`key.bin`**이 복호화되어 **`key.txt`**가 저장되었다. 

![키리커버리후_공격자파일.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dd6dcde3-9aa5-4ca0-bdf2-b214a7790a05/%ED%82%A4%EB%A6%AC%EC%BB%A4%EB%B2%84%EB%A6%AC%ED%9B%84_%EA%B3%B5%EA%B2%A9%EC%9E%90%ED%8C%8C%EC%9D%BC.png)

**[결과 : victim 의 폴더 - 변화 없음]**

![키리커버리후_피해자파일.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4c2518f-c73d-4e6c-8570-dadfb6435c37/%ED%82%A4%EB%A6%AC%EC%BB%A4%EB%B2%84%EB%A6%AC%ED%9B%84_%ED%94%BC%ED%95%B4%EC%9E%90%ED%8C%8C%EC%9D%BC.png)

(4) 복호화된 key를 가지고 피해자의 파일을 복호화한다. 

- [명령어]

```bash
cd ../victim
python3 file-recovery.py
```

**[결과 : victim 폴더 복호화 모습 - 복호화 완료]**

**`.enc 파일`**들이 복호화되어 **`.txt`**로 변환되었고 **`.enc파일`**들은 없어졌다. 

![최종피해자파일.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/37469d4b-d3a5-4a8c-885f-60020d2c2270/%EC%B5%9C%EC%A2%85%ED%94%BC%ED%95%B4%EC%9E%90%ED%8C%8C%EC%9D%BC.png)

**[결과 : attacker 파일 - 변화없음]**
