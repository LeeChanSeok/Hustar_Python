#(문제) 파일로부터 데이터를 읽어서 성적 목록을 만들어 관리하는 성적 관리 프로그램을 작성한다.
#이 프로그램은 사용자로부터 7개의 명령어(show, search, changescore, searchgrade, add, remove, quit)를 입력 받아 각 기능을 수행하게 된다.
#최소한 각 명령어 별로 함수를 정의하여 사용한다. 명령어 외에 필요한 함수는 추가로 정의하여 사용할 수 있다.

##########함수 정의##########

#처음 파일에서 학생정보를 읽어 오는 경우와 학생을 추가하는 경우 같은 기능을 함으로 하나의 함수로 정의하였다.
def is_StuID(stu_dict, stuID):
    if stuID in stu_dict:
        return True
    return False

#중간고사 점수와 기말고사 점수의 평균을 구한다.
def calc_Average(score):
    return (score[0] + score[1]) / len(score)

#평균(Average)항목은 중간고사 점수와 기말고사 점수의 평균을 계산하여 저장한다.
#학점(Grade)항목의 기준은 아래와 같다.
def calc_Grade(average):

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

#Show
def show(stu_dict):
    show_List = ['Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade']
    print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" %(show_List[0], show_List[1], show_List[2], show_List[3], show_List[4], show_List[5]))
    print("-" * 80)


    print_Student(stu_dict)
    #for stuID, stu_Info in stu_dict.items():
    #    print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (stuID, stu_Info[0], stu_Info[1], stu_Info[2], stu_Info[3], stu_Info[4]))
    '''
    for stu_Info in sorted_s1:

        print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (stu_Info[0], stu_Info[1][0], stu_Info[1][1], stu_Info[1][2], stu_Info[1][3], stu_Info[1][4]))
    '''
    #print(sorted_s1)

def print_Student(stu_dict):
    sorted_s1 = sorted(stu_dict.items(), key=lambda a: a[1][3], reverse=True)
    # for stuID, stu_Info in stu_dict.items():
    #    print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (stuID, stu_Info[0], stu_Info[1], stu_Info[2], stu_Info[3], stu_Info[4]))
    for stu_Info in sorted_s1:
        print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (
        stu_Info[0], stu_Info[1][0], stu_Info[1][1], stu_Info[1][2], stu_Info[1][3], stu_Info[1][4]))
    # print(sorted_s1)

'''
def show_person(stu_id, stu_Info):
    show_List = ['Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade']
    print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" %(show_List[0], show_List[1], show_List[2], show_List[3], show_List[4], show_List[5]))
    print("-" * 80)
    print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (stu_id, stu_Info[0], stu_Info[1], stu_Info[2], stu_Info[3], stu_Info[4]))
'''
def show_change(stu_List):
    show_List = ['Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade']
    print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" %(show_List[0], show_List[1], show_List[2], show_List[3], show_List[4], show_List[5]))
    print("-" * 80)


    print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (stu_List[0][0], stu_List[0][1], stu_List[0][2], stu_List[0][3], stu_List[0][4], stu_List[0][5]))
    print("Score changed.")
    print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (stu_List[1][0], stu_List[1][1], stu_List[1][2], stu_List[1][3], stu_List[1][4], stu_List[1][5]))




def search(stu_dict):
    try:
        stu_id = input("Student ID: ")
        searched_stu = {}
        searched_stu[stu_id] = stu_dict[stu_id]
        show(searched_stu)

    except:
        print("No SUCH PERSON.")

def changescore(stu_dict):


    termList = ['mid', 'final']

    try:
        stu_id = input("Student ID: ")

        student = []
        student.append(stu_id)
        student = student + stu_dict[stu_id]
        term = input("Mid/Final?").lower()
        if term not in termList:
            return

        score = int(input("Input new score: "))
        if score < 0 or score > 100:
            return

        sub_stu_List = []
        sub_stu_List.append(student)
        if term == 'mid':
            stu_dict[stu_id][1] = score
        else:
            stu_dict[stu_id][2] = score

        Average = calc_Average(stu_dict[stu_id][1:3])
        Grade = calc_Grade(Average)

        stu_dict[stu_id][3] = Average
        stu_dict[stu_id][4] = Grade

        newStudent = []
        newStudent.append(stu_id)
        newStudent = newStudent + stu_dict[stu_id]
        sub_stu_List.append(newStudent)
        show_change(sub_stu_List)

    except:
        print("No SUCH PERSON.")

def add(stu_dict):

    stu_id = input("Student ID: ")

    if is_StuID(stu_dict, stu_id):
        print("ALREADY EXISTS.")
        return

    stu_name = input("Name: ")
    midterm_Score = int(input("Midterm Score: "))
    fianl_Score = int(input("Final Score: "))

    Average = calc_Average([midterm_Score, fianl_Score])
    Grade = calc_Grade(Average)

    stu_dict[stu_id] = [stu_name, midterm_Score, fianl_Score, Average, Grade]

    print("Student added.")

def is_Grade(stu_dict, grade):

    grade_dict = {}

    for key, value in stu_dict.items():
        if grade in value:
            grade_dict[key] = value

    if len(grade_dict) == 0:
        print("NO RESULTS.")
        return False

    show(grade_dict)
    return True


def searchgrade(stu_dict):
    grade_List = ['A', 'B', 'C', 'D', 'F']
    grade = input("Grade to search: ")

    if grade not in grade_List:
        return

    if is_Grade(stu_dict, grade):
        return

def remove(stu_dic):
    if len(stu_dict) == 0 :
        return

    del_stuId = input("Student ID: ")
    if not is_StuID(stu_dict, del_stuId):
        print("NO SUCH PERSON.")
        return

    del(stu_dict[del_stuId])
    print("Student removed.")


def quit_():
    save = input("Save data?[yes/no] ")

    if save != 'yes':
        return

    fileName = input("File name: ")

    with open(fileName, "w") as fw:
        sorted_s1 = sorted(stu_dict.items(), key=lambda a: a[1][3], reverse=True)
        print(sorted_s1)

        for stu in sorted_s1:
            data = "%s\t%s\t%s\t%s\n" %(stu[0], stu[1][0], stu[1][1], stu[1][2])
            fw.write(data)

###########################

#프로그램 실행은 다음과 같이 한다.
#python projcet1.py students.txt

import sys

# python projcet1.py students.txt
# python 이후 작성된 문자열이 공백을 기준으로 argv 리스트에 저장된다.
# sys.argv[0] == project1.py, sys.argv[1] == students.txt

fileName = ''
try:
    fileName = sys.argv[1]
except:
    #파일명을 입력하지 않을 경우, default로 "students.txt"로부터 데이터를 읽는다.
    fileName = "students.txt"


#학생의 정보를 담을 data structure로 dictionary를 사용한다.
#학생의 학번은 고유함으로 이를 dictionary의 Key값으로 사용한다.
stu_dict = {}
#해당 파일이 존재한지 예외처리한다.

with open(fileName, "r") as fr:
    #file의 각 줄을 읽어와 변수 line에 저장한다.
    #file의 마지막 줄까지 읽어오기를 반복한다.
    for line in fr:
        #line의 마지막 줄바꿈 특수기호인 개행 문자열을('\n') 빈칸으로 바꾼다.
        #strip() 이용 시 Student Name의 이름과 성 또한 분리하기 떄문에 사용하지 않았다.
        #개행 문자열 제거 후 탭키('\t')를 기준으로 각 정보를 분리하여 List 형으로 저장한다.

        stu_Info = line.replace("\n", "")
        stu_Info = stu_Info.split("\t")

        if not is_StuID(stu_dict, stu_Info[0]):
            stu_dict[stu_Info[0]] = [stu_Info[1]]
            stu_dict[stu_Info[0]].append(int(stu_Info[2]))
            stu_dict[stu_Info[0]].append(int(stu_Info[3]))

            Average = calc_Average(stu_dict[stu_Info[0]][1:3])
            Grade = calc_Grade(Average)

            stu_dict[stu_Info[0]].append(Average)
            stu_dict[stu_Info[0]].append(Grade)

        else:
            print("이미 해당 학생이 존재합니다.")


show(stu_dict)



command_List = ['show', 'search', 'changescore', 'add','searchgrade', 'remove', 'quit']
while True:
    command = input("#").lower()

    if command not in command_List:
        continue

    if command == 'show':
        show(stu_dict)
    elif command == 'search':
        search(stu_dict)
    elif command == 'changescore':
        changescore(stu_dict)
    elif command == 'add':
        add(stu_dict)
    elif command == 'searchgrade':
        searchgrade(stu_dict)
    elif command == 'remove':
        remove(stu_dict)
    elif command == 'quit':
        quit_()
        break
