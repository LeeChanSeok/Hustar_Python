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

#함수 구현 부분
##################################################################

'''
 평균(Average)항목은 중간고사 점수와 기말고사 점수의 평균을 계산하여 저장한다.
 학점(Grade)항목의 기준은 아래와 같다.
'''
def calc_average(mid_score, final_score):
    return (mid_score + final_score) / 2

def calc_grade(average):

    grade = ''

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade


'''
전체 목록을 평균 점수를 기준으로 내림차순으로 정렬한다. 
동일한 평균 점수를 가진 학생들이 있는 경우 순서는 상관없다.

아래 함수는 학생들의 정보를 출력하기 위한 print 함수들이다.
'''
def print_Header():
    show_List = ['Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade']
    print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (
    show_List[0], show_List[1], show_List[2], show_List[3], show_List[4], show_List[5]))
    print("-" * 80)

def print_Students(sub_stu_dict):
    #입력받은 학생 정보 딕셔너리에서 평균 점수( a[1][3])를 기준으로 내림차순(reverse=True)으로 정렬하여 List로 return한다
    sorted_s1 = sorted(sub_stu_dict.items(), key=lambda a: a[1][3], reverse=True)

    for stu_Info in sorted_s1:
        print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (
        stu_Info[0], stu_Info[1][0], stu_Info[1][1], stu_Info[1][2], stu_Info[1][3], stu_Info[1][4]))

def print_Table(sub_stu_dict):
    print_Header()
    print_Students(sub_stu_dict)


##################################################################

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


    '''
    프로그램 실행 시 텍스트 파일로부터 학생들의 성적 목록 작성을 위한 데이터를 읽는다.
    각 줄은 각 학생의 학번, 이름, 중간고사 점수, 기말고사 점수로 구성되어 있으며 
    각 항목 사이는 tab(\t)으로 구분된다.
     학생과 학생 사이는 줄 바꿈 문자(\n)으로 구분된다.
        Ex. [Student number][\t][Name][\t][Midterm][\t][Final][\n]
     프로그램을 실행시키면 텍스트 파일로부터 데이터를 읽어 
     목록을 리스트(list) 자료형 또는 딕셔너리(dict) 자료형을 사용하여 저장하고,
     전체 목록을 평균 점수를 기준으로 내림차순으로 정렬하여 아래의 예제처럼 출력한다. 
     동일한 평균 점수를 가진 학생들이 있는 경우 순서는 상관없다.
    '''

    #텍스트 파일로부터 읽은 데이터를 딕셔너리 자료형을 사용하여 저장한다.
    #학생의 학번은 고유한 값이므로 이를 딕셔너리의 Key 값으로 사용한다.
    stu_dict = {}
    with open(fileName, "r") as fr:
        for line in fr:
            line = line.replace("\n", "")
            stu_data = line.split("\t")

            '''
            stu_data[0] == [Student number]
            stu_data[1] == [Name]
            stu_data[2] == [Midterm]
            stu_data[3] == [Final]
            '''

            stu_dict[stu_data[0]] = [stu_data[1]]
            stu_dict[stu_data[0]].append(int(stu_data[2]))
            stu_dict[stu_data[0]].append(int(stu_data[3]))

            average = calc_average(stu_dict[stu_data[0]][1], stu_dict[stu_data[0]][2])
            grade = calc_grade(average)

            stu_dict[stu_data[0]].append(average)
            stu_dict[stu_data[0]].append(grade)

    print_Table(stu_dict)

    '''
    위와 같이 학생들의 성적 목록이 출력 된 후에는 명령어 입력을 대기하는 #표시가 뜨며,
    이 상태에서 사용자는 명령어를 입력할 수 있다.
     사용자는 7개의 명령어(show, search, changescore, searchgrade, add, remove, quit)를
    사용할 수 있으며, 명령어를 입력하였을 때만 기능이 실행된다. 이 명령어는 사용자가 명령어 입력 시, 
    대소문자를 구분하지 않고 동일한 명령어의 기능을 수행하도록 작성한다. 
    예를 들면, show, SHOW, Show, shoW 는 동일한 동작을 수행한다.
     7개의 명령어 이외의 잘못된 명령어 입력 시, 에러 메시지 없이 다시 명령어를 입력 받을 준비를 한다.
    '''


    # 사용자는 아래 7개의 명령어를 사용할 수 있다.
    command_List = ['show', 'search', 'changescore', 'searchgrade', 'add', 'remove', 'quit']
    while True:
        # 명령어는 대소문자를 구분하지 않는다. 따라서, 입력받은 명령어를 모두 소문자로 바꾸었다.
        command = input("# ").lower()

        #잘못된 명령어 입력 시, 에러 메시지 없이 다시 명령어를 입력 받을 준비를 한다.
        if command not in command_List:
            continue



# main함수가 있으면 main함수를 실행한다.
if __name__ == "__main__":
    main()

