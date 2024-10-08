# DFdetecter
당신의 사진변조를 찾아냅니다.
<span style="color: red;">**본 서비스는 맹신할만큼의 정확성을 가지고 있지 않습니다. 다양한 신뢰 가능한 서비스를 통해 판단하시기 바랍니다. 오직 참조 목적으로만 이용해주세요.**</span>


## 사용법
1. 이 코드를 clone 또는 fork 등으로 다운로드합니다.
2. cmd에 ``pip install -r "requirements.txt"``를 사용해 모듈을 설치합니다.
3. .env를 생성한후 googleAPI, googleCustomEngine값을 추가하세요. (googleAPI=) 그런다음 키를 입력하세요. 키 입력방법은 하단에서 후술합니다.
4. python3 server.py를 터미널(cmd)에 입력합니다.

## 안내
### 라이센스 관련
해당 레포지토리는 `무라이선스`를 준수합니다.
만약 해당 오픈소스를 사용하시거나 수정하고 싶으시다면 자유롭게 사용하실 수 있습니다.

+ 단 본 소스코드는 피해자를 위해 제작된 코드이므로 악의적 목적으로 악용음 엄격히 금합니다.

---

### 키발급방법

1. **Google Cloud Platform에서 API 키 발급받기**

   1. [Google Cloud Console](https://console.cloud.google.com/)에 로그인합니다.
   2. **프로젝트 생성**:
      - 좌측 상단의 **프로젝트 선택** 버튼을 클릭하고 **새 프로젝트**를 선택하여 새로운 프로젝트를 생성합니다.
      - 프로젝트 이름을 입력하고 **만들기**를 클릭합니다.
   3. **API 활성화**:
      - 새 프로젝트에서 **API 및 서비스** > **라이브러리**로 이동합니다.
      - **Google Cloud Vision API**를 검색하고 **사용** 버튼을 클릭하여 API를 활성화합니다.
      - 또한 **Custom Search API**를 검색하여 활성화합니다.
   4. **API 키 생성**:
      - **API 및 서비스** > **사용자 인증 정보**로 이동합니다.
      - **사용자 인증 정보 만들기** 버튼을 클릭하고 **API 키**를 선택하여 새로운 API 키를 생성합니다.
      - 생성된 API 키를 복사하여 `.env` 파일에 추가합니다.

2. **Google Custom Search Engine(CSE) 설정**

   1. [Google Custom Search Engine](https://cse.google.com/cse/) 페이지로 이동합니다.
   2. **새 검색 엔진 만들기** 버튼을 클릭합니다.
   3. **사이트 검색**란에 검색할 사이트를 입력합니다 (예: `nintendo.com` 또는 특정 사이트).
   4. 검색 엔진의 이름을 입력하고 **만들기**를 클릭합니다.
   5. **검색 엔진 ID(CX) 확인**:
      - 생성된 검색 엔진 목록에서 **제어판**을 클릭합니다.
      - **기본 설정**에서 **검색 엔진 ID**를 찾을 수 있습니다. 이 값을 복사하여 `.env` 파일에 추가합니다.
   6. **검색 엔진 활성화**:
      - **기본 설정**에서 검색 엔진의 **비즈니스 이메일**과 **자동으로 검색 결과 사용 허가**를 활성화합니다.

3. **.env 파일 설정**

   `.env` 파일에 발급받은 API 키와 Custom Search Engine ID를 입력합니다.
---

### 기여
기여는 자유입니다.
#### 기여 방법
1. [해당 레포지토리를 포크](https://github.com/12302a/DFdetecter/fork)합니다.
2. 포크된 레포지토리에서 자유롭게 코드를 수정합니다.
3. [해당 레포지토리에 PR을 남깁니다.](https://github.com/12302a/DFdetecter/pulls)
---

### 문의사항 
소스코드 사용에 관한 어려움이 있으신가요? [인스타그램](https://www.instagram.com/12302a_?igsh=MWgxNzZ6eWhmMmVrcw==)에 남겨주세요!
---

## 버그제보 받습니다. [이슈](https://github.com/12302a/DFdetecter/issues) 남겨주세요!


