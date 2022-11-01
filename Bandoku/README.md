# Bandoku
```
너무 귀찮아요
```

## 실행
사용하기에 앞서, [데스크톱용 Chrome](https://www.google.com/intl/ko/chrome/) 및 [ChromeDriver](https://chromedriver.chromium.org/home)(이)가 필요합니다.
```
1. 데스크톱용 Chrome 설치 프로그램을 실행하여 설치합니다.
2. 주소 표시줄에 'chrome://version/'을 입력하여 현재 데스크톱용 Chrome의 버전을 확인합니다.
3. 데스크톱용 Chrome 버전에 맞는 ChromeDriver(을)를 다운로드해줍니다.
4. 다운로드한 파일을 패키지의 'Driver' 폴더에 삽입합니다.
```
Python 릴리즈의 경우, [Python3](https://www.python.org/) 및 Selenium(이)가 추가로 필요합니다.
```
1. 'Python3.x.x' 설치 프로그램을 다운로드해 설치합니다.
2. '명령 프롬프트(cmd)'를 열어 "pip3 install Selenium"(을)를 입력하고 설치가 완료될 때까지 기다립니다.
```
## 기타
'ChromeDriver'의 Console(을)를 완전히 꺼버리고 싶다면, 다음과 같이 조치 가능합니다.
```
1. "(Python 설치경로)\Python38-32\Lib\site-packages\selenium\webdriver\common" 경로를 찾아 폴더를 엽니다.
2. 'service.py' 파일을 수정하여, 'subprocess.Popen' 함수의 마지막 인자로 'creationflags=0x08000000'를 추가하고 저장합니다.
```
```python
self.process = subprocess.Popen(cmd, env=self.env,
                                close_fds=platform.system() != 'Windows',
                                stdout=self.log_file,
                                stderr=self.log_file,
                                stdin=PIPE, # 쉼표 유무 주의
                                creationflags=0x08000000) # 인자 추가
```
