'''
성적 관리 프로그램
과제 제출 마감일: 2020-08-12 23:59

(문제)
파일로부터 데이터를 읽어서 성적 목록을 만들어 관리하는 성적 관리 프로그램을 작성한다.

(주의사항)
 이 프로그램은 사용자로부터 7개의 명령어
(show, search, changescore, searchgrade, add, remove, quit)를 입력 받아 각 기능을 수행 하게 된다.
최소한 각 명령어 별로 함수를 정의하여 사용한다. 명령어 외에 필요한 함수는 추가로 정의하여 사용할 수 있다.
 소스코드 제출파일이름은 “project1_3.py”로 한다.
 보고서 파일은 project1.doc(x) 로 한다. 보고서 작성에 대한 설명은 마지막 페이지에 있으니 아래의 문제를 풀기 전, 먼저 확인하도록 한다.
 기본적으로 문제에서 요구한 사항대로 구현을 하되, 실제로 프로그램을 작성하다 보면 결정해야 할 세부 사항이 많아진다.
명시되어 있지 않은 세부사항에 대해서 처리한 방법, 이유 등을 보고서에 기록하도록 한다.
'''

import sys

# 학생 및 학생 관리 클래스 생성
class Student:
    def __init__(self, stu_id, stu_name, stu_mid_score, stu_final_score):
        self.id = stu_id
        self.name = stu_name
        self.mid_score = stu_mid_score
        self.final_score = stu_final_score
        self.average = self.calc_average()
        self.grade = self.calc_grade()

    '''
     평균(Average)항목은 중간고사 점수와 기말고사 점수의 평균을 계산하여 저장한다.
     학점(Grade)항목의 기준은 아래와 같다.
    '''
    def calc_average(self):
        return (self.mid_score + self.final_score) / 2

    def calc_grade(self):
        if self.average >= 90:
            grade = 'A'
        elif self.average >= 80:
            grade = 'B'
        elif self.average >= 70:
            grade = 'C'
        elif self.average >= 60:
            grade = 'D'
        else:
            grade = 'F'

        return grade

    def update(self):
        self.average = self.calc_average()
        self.grade = self.calc_grade()

    def print_Student(self):
        print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (
            self.id, self.name, self.mid_score, self.final_score, self.average, self.grade))

class StudentMgr:

    def __init__(self):
        self.students = {}
        self.Num_student = 0

    def AddStudent(self, student):
        if student.id in self.students:
            return
        self.students[student.id] = student
        self.Num_student += 1
    '''
    전체 목록을 평균 점수를 기준으로 내림차순으로 정렬한다.
    동일한 평균 점수를 가진 학생들이 있는 경우 순서는 상관없다.

    아래 함수는 학생들의 정보를 출력하기 위한 print 함수들이다.
    '''
    def print_Header(self):
        show_List = ['Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade']
        print("%8s\t%15s\t\t%7s\t\t%5s\t\t%8s\t\t%5s" % (
            show_List[0], show_List[1], show_List[2], show_List[3], show_List[4], show_List[5]))
        print("-" * 100)

    def print_Students(self, sub_student):
        # 입력받은 학생 정보 딕셔너리에서 평균 점수( a[1][3])를 기준으로 내림차순(reverse=True)으로 정렬하여 List로 return한다
        sorted_sub_dict = sorted(sub_student.values(), key=lambda a: a.average, reverse=True)

        for student in sorted_sub_dict:
            student.print_Student()

    def print_Table(self, sub_student):
        self.print_Header()
        self.print_Students(sub_student)

    '''
    (기능)
         성적 관리 프로그램은 아래와 같은 기능을 가진다.
         명시된 7가지 명령어 외의 명령어가 입력될 경우 무시하고 다시 명령어 입력을 대기한다.
    '''
    # 기능 관련 함수들
    '''
     1. show (전체 학생 정보 출력)
          show 입력 시, 저장되어 있는 전체 목록을 아래와 같이 평균 점수를 기준으로 내림차순으로 출력한다. 
         평균 점수는 소수점 이하 첫째 자리까지만 표시한다.
    '''

    # 1. show (전체 학생 정보 출력)
    # 입력받은 dict에 저장된 Student 정보들을 출력한다.
    def Show(self):
        self.print_Table(self.students)

    '''
     2. search (특정 학생 검색)
          search 입력 시, 아래와 같이 검색하고자 하는 학생의 학번을 요구해 입력 받아 학번,
         이름, 중간고사 점수, 기말고사 점수, 평균, 학점을 출력한다.
          예외처리:
          찾고자 하는 학생이 목록에 없는 경우에는 “NO SUCH PERSON.” 이라는 에러 메시지를 출력
    '''

    # 학번을 입력받아 예외처리하는 기능이 자주 사용됨으로 하나의 함수로 만들어 재사용성을 높이려 하였다.
    # 학번을 입력받아 학생 딕셔너리에 존재하면 True, 존재하지 않으면 False 를 return 한다.
    def is_StuId(self, stu_Id):
        if stu_Id not in self.students:
            return False
        return True

    # 2. search (특정 학생 검색)
    # 입력받은 아이디에 해당하는 학생이 있는 경우, 해당 아아디를 Key값으로 학생의 정보를 담은 딕셔너리를 만든다.
    # 이 딕셔너리를 기존에 학생정보를 출력하기 위해 만들었던 함수에 매개변수로 전달하여 학생정보를 출력한다.
    def Search(self):

        stu_Id = input("Student ID: ")
        if not self.is_StuId(stu_Id):
            print("No SUCH PERSON.")
            return

        student = {}
        student[stu_Id] = self.students[stu_Id]
        self.print_Table(student)

    '''
    3. changescore (점수 수정)
         목록에 저장된 학생 중 1명의 중간고사(mid) 혹은 기말고사(final)의 점수를 수정한다.
         changescore 입력 시, 수정하고자 하는 학생의 학번, 수정하고자 하는 점수가
        중간고사인지 기말고사인지와 수정하고자 하는 점수를 순서대로 입력 받아 해당 학생의 점수를 수정한다.
         점수가 바뀜에 따라 Grade도 다시 계산하여 수정한다.
         예외처리:
             학번이 목록에 없는 경우에는 “NO SUCH PERSON.”이라는 에러 메시지를 출력
             “mid” 또는 “final” 외의 값이 입력된 경우에는 실행되지 않음
             점수에 0~100 외의 값이 입력된 경우에는 실행되지 않음
    '''

    # 시험점수를 입력받아 예외처리하는 기능이 자주 사용됨으로 하나의 함수로 만들어 재사용성을 높이려 하였다.
    # 시험점수를 입력받아 0~100 사이의 숫자인 경우만 처리하도록 한다.
    def in_Score(self, score):
        if score < 0 or score > 100:
            return False
        return True

    # 3. changescore (점수 수정)
    # 학번, 시험기간, 점수 에 대한 예외 처리 후 학생 점수를 수정하고 평균과 성적 또한 수정한다.
    def ChangeScore(self):
        stu_Id = input("Student ID: ")
        if not self.is_StuId(stu_Id):
            print("No SUCH PERSON.")
            return

        Term_dict = ['mid','final']
        term = input("Mid/Final? ").lower()

        # “mid” 또는 “final” 외의 값이 입력된 경우에는 실행되지 않음
        if term not in Term_dict:
            return
        # 점수에 0~100 외의 값이 입력된 경우에는 실행되지 않음
        score = int(input("Input new score: "))
        if not self.in_Score(score):
            return

        # 수정되기 전의 학생 정보를 출력하기 전에 딕셔너리에 현재의 값을 저장하고 출력한다
        preb_student = {}
        preb_student[stu_Id] = self.students[stu_Id]
        self.print_Table(preb_student)
        print("Score changed.")

        # 입력받은 점수가 해당하는 시험의 점수를 변경한다.
        if term == 'mid':
            self.students[stu_Id].mid_score = score
        else:
            self.students[stu_Id].final_score = score
        self.students[stu_Id].update()

        # 변경된 학생 정보를 출력한다.
        changed_student = {}
        changed_student[stu_Id] = self.students[stu_Id]
        self.print_Students(changed_student)

    '''
    4. add (학생 추가)
         add 입력 시, 아래와 같이 학생의 학번, 이름, 중간고사 점수, 기말고사 점수를 차례로 요구해 입력 받는다. 
        추가되면, 메시지 “Student added.”를 아래 예제와 같이 출력한다.
         Average와 Grade는 중간고사 점수와 기말고사 점수를 사용하여 계산하여 저장한다.
         학생 추가 후 show 명령어를 사용하면 평균을 기준으로 내림차순으로 출력된다.
         에러처리:
         목록에 있는 학생의 학번을 입력 시, ‘ALREADY EXISTS.’ 이라는 에러 메시지 출력
    '''

    # 4. add(학생추가)
    def Add(self):
        stu_Id = input("Student ID: ")
        # 목록에 있는 학생의 학번을 입력 시, ‘ALREADY EXISTS.’ 이라는 에러 메시지 출력
        if self.is_StuId(stu_Id):
            print("ALREADY EXISTS")
            return

        stu_Name = input("Name: ")

        # 입력받은 점수가 0~100사이의 점수인지 확인한다
        midTerm_Score = int(input("Midterm Score: "))
        if not self.in_Score(midTerm_Score):
            print("해당 점수가 범위(0~100)를 벗어났습니다")
            return

        finalTerm_Score = int(input("Final Score: "))
        if not self.in_Score(finalTerm_Score):
            print("해당 점수가 범위(0~100)를 벗어났습니다")
            return

        student = Student(stu_Id, stu_Name, midTerm_Score, finalTerm_Score)

        self.AddStudent(student)
        print("Student added.")

    '''
    5. searchgrade (Grade 검색)
         searchgrade입력 시, 특정 grade를 입력 받아 그 grade에 해당하는 학생을 모두 출력한다.
         예외처리:
             A, B, C, D, F 외의 값이 입력된 경우 실행되지 않음.
             해당 grade 의 학생이 없는 경우 아래와 같이 메시지 “NO RESULTS.” 출력
    '''
    # grade를 입력받아 해당 grade에 해당하는 학생 정보를 딕셔너리에 저장한다.
    def grade_student(self, grade):
        grade_student = {}

        for key, value in self.students.items():
            if grade == value.grade:
                grade_student[key] = value

        return grade_student

    # 5. searchgrade (Grade 검색)
    def SearchGrade(self):
        grade_List = ['A', 'B', 'C', 'D', 'F']

        grade = input("Grade to search : ")
        # A, B, C, D, F 외의 값이 입력된 경우 실행되지 않음.
        if grade not in grade_List:
            return

        students = self.grade_student(grade)
        # 해당 grade 의 학생이 없는 경우 아래와 같이 메시지 “NO RESULTS.” 출력
        if len(students) == 0:
            print("NO RESULTS.")
            return
        # 특정 grade에 해당하는 학생을 모두 출력한다.
        self.print_Table(students)

    '''
    6. REMOVE (특정 학생 삭제)
         remove 입력 시, 아래와 같이 삭제하고자 하는 학생의 학번을 입력 받은 후, 학생이 목록에 있는 경우 삭제한다. 
        삭제하면, 메시지 “Student removed.”를 아래와 같이 출력한다.
         예외처리:
         목록에 아무도 없을 경우 아래의 예제와 같이 “List is empty.” 메시지 출력
    '''
    # 6. REMOVE (특정 학생 삭제)
    def Remove(self):
        # 목록에 아무도 없을 경우 아래의 예제와 같이 “List is empty.” 메시지 출력
        if self.Num_student == 0:
            print("List is empty.")
            return

        stu_Id = input("Student ID: ")
        if not self.is_StuId(stu_Id):
            print("No SUCH PERSON.")
            return

        # 삭제하면, 메시지 “Student removed.”를 아래와 같이 출력한다.
        del (self.students[stu_Id])
        print("Student removed.")
        self.Num_student -=1

    '''
    7. quit (종료)
         quit 입력 시, 프로그램을 종료한다.
         해당 명령어를 실행할 경우, 현재까지 편집할 내용의 저장 여부를 묻고, 저장을 선택할 경우 파일명을 입력 받아서 저장하도록 한다. 
        앞서 본 “students.txt”와 같이 내용을 구성한다.
        [Student number][\t][Name][\t][Midterm][\t][Final][\n]
         저장할 때 목록의 순서는 평균을 기준으로 내림차순으로 한다.
         파일 이름에는 공백이 없다고 가정한다.
    '''
    # 7. quit (종료)
    def Quit(self):
        save = input("Save data?[yes/no] ").lower()

        if save != 'yes':
            return

        fileName = input("File name: ")

        with open(fileName, "w") as fw:
            sorted_stu_dict = sorted(self.students.values(), key=lambda a: a.average, reverse=True)

            for student in sorted_stu_dict:
                data = "%s\t%s\t%d\t%d\t\n" % (student.id, student.name, student.mid_score, student.final_score)
                fw.write(data)

'''
(설명)
 프로그램 실행은 다음과 같이 한다. (실행예시에 밑줄로 표시된 문자는 사용자 입력에 해당)
     리눅스의 경우
    $ python project1_3.py students.txt
     윈도우의 경우
    C:\>python project1_3.py students.txt
 파일명을 입력하지 않을 경우, default로 “students.txt”로부터 데이터를 읽는다.
 파일명이 입력될 경우, 입력된 파일로부터 데이터를 읽는다.
 파일명에는 공백이 없다고 가정한다. (즉, 공백이 있는 파일명의 입력에 대해서는 고려하지 않는다.
'''

def main():
    # $ python project1_3.py students.txt
    # project1_3.py == sys.argv[0], students.txt == sys.argv[1]

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
    global studentsMgr
    studentsMgr = StudentMgr()

    try:
        with open(fileName, "r") as fr:
            # file의 각 줄을 읽어와 변수 line에 저장한다.
            # file의 마지막 줄까지 읽어오기를 반복한다.
            for line in fr:
                # line의 마지막 줄바꿈 특수기호인 개행 문자열을('\n') 빈칸으로 바꾼다.
                # strip() 이용 시 Student Name의 이름과 성 또한 분리하기 떄문에 사용하지 않았다.
                # 개행 문자열 제거 후 탭키('\t')를 기준으로 각 정보를 분리하여 List 형으로 저장한다.
                line = line.replace("\n", "")
                stu_data = line.split("\t")

                stu_Id = stu_data[0]
                stu_Name = stu_data[1]
                midTerm_Score = int(stu_data[2])
                finalTerm_Score = int(stu_data[3])

                student = Student(stu_Id, stu_Name, midTerm_Score, finalTerm_Score)
                studentsMgr.AddStudent(student)

        studentsMgr.print_Table(studentsMgr.students)
    except:
        print("해당 파일이 존재하지 않습니다.")
        return 0

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
        command = input("\n# ").lower()

        #잘못된 명령어 입력 시, 에러 메시지 없이 다시 명령어를 입력 받을 준비를 한다.
        if command not in command_List:
            continue

        '''
        (기능) 
        1. show (전체 학생 정보 출력) 
        2. search (특정 학생 검색)
        3. changescore (점수 수정)
        4. add (학생 추가)
        5. searchgrade (Grade 검색)
        6. remove (특정 학생 삭제)
        7. quit (종료)
        '''

        if command == 'show':
            studentsMgr.Show()
        elif command == 'search':
            studentsMgr.Search()
        elif command == 'changescore':
            studentsMgr.ChangeScore()
        elif command == 'add':
            studentsMgr.Add()
        elif command == 'searchgrade':
            studentsMgr.SearchGrade()
        elif command == 'remove':
            studentsMgr.Remove()
        elif command == 'quit':
            studentsMgr.Quit()
            break

# main함수가 있으면 main함수를 실행한다.
if __name__ == "__main__":
    main()

