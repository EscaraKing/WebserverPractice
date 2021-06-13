#!/usr/bin/python

'''
CGI 기본적인 apache2와의 연동방법
1. apache2 설정파일에 들어가 .py을 인식하고
인실할 다이렉토리를 지정해준다
2. CGI모듈을 다운 받고 서버를 재시작시켜준다
3. content-type:text/html을 사용하면
    그 다음에 나올 내용이 html파일의 내용임을
    지정해줄 수 있다 
'''

import cgi
if __name__ == "__main__":
    #content-type:text/html은 다음에 나올 내용이
    #thml컨텐츠로 받아들이라는 뜻이다 
    print("content-type:text/html; charset=UTF-8\n")
    print(1+1)