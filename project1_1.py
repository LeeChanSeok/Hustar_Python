'''
성적 관리 프로그램
과제 제출 마감일: 2020-08-12 23:59

(문제)
파일로부터 데이터를 읽어서 성적 목록을 만들어 관리하는 성적 관리 프로그램을 작성한다.

(주의사항)
 이 프로그램은 사용자로부터 7개의 명령어
(show, search, changescore, searchgrade, add, remove, quit)를 입력 받아 각 기능을 수행 하게 된다.
최소한 각 명령어 별로 함수를 정의하여 사용한다. 명령어 외에 필요한 함수는 추가로 정의하여 사용할 수 있다.
 소스코드 제출파일이름은 “project1.py”로 한다.
 보고서 파일은 project1.doc(x) 로 한다. 보고서 작성에 대한 설명은 마지막 페이지에 있으니 아래의 문제를 풀기 전, 먼저 확인하도록 한다.
 기본적으로 문제에서 요구한 사항대로 구현을 하되, 실제로 프로그램을 작성하다 보면 결정해야 할 세부 사항이 많아진다.
명시되어 있지 않은 세부사항에 대해서 처리한 방법, 이유 등을 보고서에 기록하도록 한다.
'''



'''
(설명)
 프로그램 실행은 다음과 같이 한다. (실행예시에 밑줄로 표시된 문자는 사용자 입력에 해당)
     리눅스의 경우
    $ python project1.py students.txt
     윈도우의 경우
    C:\>python project1.py students.txt
 파일명을 입력하지 않을 경우, default로 “students.txt”로부터 데이터를 읽는다.
 파일명이 입력될 경우, 입력된 파일로부터 데이터를 읽는다.
 파일명에는 공백이 없다고 가정한다. (즉, 공백이 있는 파일명의 입력에 대해서는 고려하지 않는다.
'''

import sys

def main():
    # $ python project1.py students.txt
    # project1.py == sys.argv[0], students.txt == sys.argv[1]

    try:
        fileName = sys.argv[1]
    except:
        fileName = "students.txt"

    print(fileName)

# main함수가 있으면 main함수를 실행한다.
if __name__ == "__main__":
    main()

