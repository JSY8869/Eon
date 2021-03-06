#기차 예매 프로그램
import numpy as np
import datetime
import os

class reservation:      #시간 출발역 도착역 열차종류
    def __init__(self):
        self.time = []      # 입력받은 시간
        self.time_temp = None  # 입력받은 시간을 시간값으로 변경
        self.time_list_temp = None # 원하는 조건에 해당하는 시간들
        self.result_list_temp = [] # 조건에 해당하는 값들 중 가장 가까운 값을 구할 때 사용할 리스트
        self.result_up_list_temp = [] # 입력받은 시간보다 낮은값이 가장 가까울 경우 높은값중 가장 가까운 값을 구할 때 사용할 리스트
        self.result_down_list_temp = [] # 입력받은 시간보다 높은값이 가장 가까울 경우 낮은값중 가장 가까운 값을 구할 때 사용할 리스트
        self.start = None # 출발역 입력
        self.arrive =None # 도착역 입력
        self.kind = None # 열차종류 입력
        self.f = None # 기차정보
        self.line = None # 기차정보를 저장한 값
        self.idx = None # 가장 가까운 값이 몇번째 줄인지 나타내는 수
        self.idx_down = None # 낮은 값중 가장 가까운 값의 줄
        self.idx_up = None # 높은 값중 가장 가까운 값의 줄
        self.line_1_temp = None # 가장 가까운 값이 몇번째 줄인지 나타내는 수를 저장하는 값
        self.line_2_temp = None # 2번째로 가까운 값을 저장
        self.updown_temp = None # 2번째로 가까운 값을 구하기 위한 조건에 해당하는 값들의 리스트
        self.listplz = None # 선택한 기차표의 좌석을 계산할 때 사용
        self.listplz2 = None # 선택한 기차표를 보기좋게 출력하기 위한 공간
        self.nono = None # 취소 선택지
        self.lines = None # 기차정보를 저장할 공간
        self.f = None # 새로 바뀌는 기차정보


    def train(self): # 1번 입력 함수
        while True:
            try:
                self.time = str(input("시간을 입력하세요  (ex) 08:00) :"))
                self.time_temp = datetime.datetime.strptime(self.time, '%H:%M')
                self.start= str(input("출발역을 입력하세요: "))
                self.arrive = str(input("도착역을 입력하세요: "))
                self.kind = str(input("열차종류를 입력하세요: "))
                self.kind = self.kind.upper()
                print("{} {} -> {} {}".format(self.time,self.start,self.arrive,self.kind))
                break
            except:
                print("다시 입력하세요")
        
    def openit(self,f): # 시간비교
        for i in range(1,21):                   #선택한 시간과 가장 가까운 시간의 기차표를 구하는 함수
            str(f[i]).split()
            self.time_list_temp = datetime.datetime.strptime(f[i].split()[0], '%H:%M')
            if self.start == str(f[i]).split()[1] and self.arrive == str(f[i]).split()[3] and self.kind == str(f[i]).split()[4]:
                self.result_list_temp.append(self.time_list_temp)

        for i in range(1,21):
            str(f[i]).split()
            self.time_list_temp = datetime.datetime.strptime(f[i].split()[0], '%H:%M')

            if self.start == str(f[i]).split()[1] and self.arrive == str(f[i]).split()[3] and self.kind == str(f[i]).split()[4]:
                self.result_list_temp = np.asarray(self.result_list_temp)
                self.idx = (np.abs(self.result_list_temp - self.time_temp)).argmin()

                if self.result_list_temp[self.idx] == self.time_list_temp:
                    print(f[i])
                    self.line_1_temp = i

        if self.result_list_temp[self.idx] < self.time_temp:

            for i in range(self.line_1_temp+1,21):                   #선택한 시간과 두번째로 가까운 시간의 기차표를 구하는 함수
                str(f[i]).split()
                self.time_list_temp = datetime.datetime.strptime(f[i].split()[0], '%H:%M')

                if self.start == str(f[i]).split()[1] and self.arrive == str(f[i]).split()[3] and self.kind == str(f[i]).split()[4]:
                    self.result_up_list_temp.append(self.time_list_temp)

            for l in range(self.line_1_temp+1,21):
                str(f[l]).split()
                self.time_list_temp = datetime.datetime.strptime(f[l].split()[0], '%H:%M')

                if self.start == str(f[l]).split()[1] and self.arrive == str(f[l]).split()[3] and self.kind == str(f[l]).split()[4]:
                    self.result_up_list_temp = np.asarray(self.result_up_list_temp)
                    self.idx_up = (np.abs(self.result_up_list_temp - self.time_temp)).argmin()

                    if self.result_up_list_temp[self.idx_up] == self.time_list_temp:
                        print(f[l])
                        self.line_2_temp = l

        elif self.result_list_temp[self.idx] > self.time_temp:

            for i in range(1,self.line_1_temp-1):                   #선택한 시간과 두번째로 가까운 시간의 기차표를 구하는 함수
                str(f[i]).split()
                self.time_list_temp = datetime.datetime.strptime(f[i].split()[0], '%H:%M')

                if self.start == str(f[i]).split()[1] and self.arrive == str(f[i]).split()[3] and self.kind == str(f[i]).split()[4]:
                    self.result_down_list_temp.append(self.time_list_temp)

            for l in range(1,self.line_1_temp-1):
                str(f[l]).split()
                self.time_list_temp = datetime.datetime.strptime(f[l].split()[0], '%H:%M')

                if self.start == str(f[l]).split()[1] and self.arrive == str(f[l]).split()[3] and self.kind == str(f[l]).split()[4]:
                    self.result_down_list_temp = np.asarray(self.result_down_list_temp)
                    self.idx_down = (np.abs(self.result_down_list_temp - self.time_temp)).argmin()

                    if self.result_down_list_temp[self.idx_down] == self.time_list_temp:
                        print(f[l])
                        self.line_2_temp = l
        

    def choose(self,f): # 위에꺼 예약
        if str(f[self.line_1_temp].split()[5]) == '매진':
            print("매진이어서 예약할 수 없습니다.")
            return(f)
        else:
            t = '매진'
            q = '0'
            f[self.line_1_temp] = f[self.line_1_temp].replace(f[self.line_1_temp].split()[5],str(int(f[self.line_1_temp].split()[5]) - 1))
            if int(f[self.line_1_temp].split()[5]) == 0:
                f[self.line_1_temp] = f[self.line_1_temp].replace(f[self.line_1_temp].split()[5],t)
                f[self.line_1_temp] = f[self.line_1_temp].replace(f[self.line_1_temp].split()[5],q,1)
            print("예약 완료")
            print(f[self.line_1_temp])
            return(f)

    def choose_list1(self,choose_list):
        choose_list.append(self.line_1_temp)
        return (choose_list)

    def temp1(self,f):
        return f[self.line_1_temp]

    def choose2(self,f): # 아래꺼 예약
        if int(f[self.line_2_temp].split()[5]) == 0:
            print("매진이어서 예약할 수 없습니다.")
            return(f)
        else:
            t = '매진'
            q = '0'
            f[self.line_2_temp] = f[self.line_2_temp].replace(f[self.line_2_temp].split()[5],str(int(f[self.line_2_temp].split()[5]) - 1))
            if int(f[self.line_2_temp].split()[5]) == 0:
                f[self.line_2_temp] = f[self.line_2_temp].replace(f[self.line_2_temp].split()[5],t)
                f[self.line_2_temp] = f[self.line_2_temp].replace(f[self.line_2_temp].split()[5],q,1)
            print(f[self.line_2_temp])
            return(f)

    def temp2(self,f):
        return f[self.line_2_temp]

    def choose_list2(self,choose_list):
        choose_list.append(self.line_2_temp)
        return (choose_list)


    def confirm(self,f,list_temp,choose_list): # 예매 취소
            while True:
                self.nono = int(input("취소하시겠습니까(예1 ,아니오2,뒤로가기3): "))
                if self.nono == 1:
                    while True:
                        try:
                            for i in range (1,len(list_temp)+1,1):
                                print(i)
                                print(list_temp[i-1])
                            while True:
                                choice = int(input("삭제하고자 하는 표를 입력하세요(0을 입력 = 뒤로가기 : "))
                                if choice != 0:
                                    try:
                                        if str(f[choose_list[choice - 1]].split()[5]) != '매진':
                                            f[choose_list[choice - 1]] = f[choose_list[choice - 1]].replace(f[choose_list[choice - 1]].split()[5],str(int(f[choose_list[choice - 1]].split()[5]) + 1))
                                            list_temp.pop(choice - 1)
                                            choose_list.pop(choice - 1)
                                            print("취소 완료")
                                            break
                                        else:
                                            f[choose_list[choice - 1]] = f[choose_list[choice - 1]].replace(f[choose_list[choice - 1]].split()[5],str(1))
                                            list_temp.pop(choice - 1)
                                            choose_list.pop(choice - 1)
                                            print("취소 완료")
                                            break
                                    except:
                                        print("다시 입력하세요")
                                elif choice == 0:
                                    break                    
                            return f
                        except:
                            print("다시 입력하세요")
                    break
                elif self.nono == 2:
                    return f
                elif self.nono == 3:
                    return f
                else:
                    print("1~2 사이의 값을 입력하세요")
    def confirm1(self,list_temp):
        return list_temp
    def confirm2(self,choose_list):
        return choose_list    

    def check(self,checkList): # 예매현황 보여주기
        print("예약 현황입니다.")
        print(checkList)
            

                    
    def whole(self,f): # 기차정보 보여주기
        for i in range(21):
            print(f[i])
    def whole2(self,line):
        for i in range(21):
            print(line[i])

f = open("C:/Users/Jason/Desktop/E-on/.vscode/library/TrainList.txt",'r')
f = f.readlines()
choice_list = []
temp_x = 0
temp = 0
for i in range(1,21,1):
    f[i].split()
list_temp = []
while(True):
    a = reservation()
    vari1 = int(input("메뉴를 입력해수세요(1:예약, 2:기차정보, 3:예매현황 및 취소, 4:프로그램 종료): ")) # 메인 메뉴
    if vari1 == 4:
        print("프로그램 종료")
        break
    if vari1 == 1:
        a.train()
        a.openit(f)
        while True:
            dothis = int(input("위에꺼 예약1,아래꺼 예약2,뒤로가기3: "))
            if dothis == 1:
                try:
                    temp = a.choose(f) # 예약한 기차정보
                    if temp == temp_x:
                        break
                    else:
                        list_temp.append(a.temp1(f)) # 예약한 기차표
                        choice_list = a.choose_list1(choice_list)
                        temp_x = temp
                        break
                except:
                    print("예매할 표가 없습니다.")
                    break
            elif dothis == 2:
                try:
                    temp = a.choose2(f)
                    if temp == temp_x:
                        break
                    else:
                        temp_x = temp
                        list_temp.append(a.temp2(f))
                        choice_list = a.choose_list2(choice_list)
                        break
                except:
                    print("예매할 표가 없습니다.")
                    break
            elif dothis == 3:
                break
            else:
                print("1~3사이의 값을 입력하세요")
    elif vari1 == 2:
            a.whole(f)
    elif vari1 == 3:
        while True:
            thatnono = int(input("예약 현황을 확인하시겠습니까? 1 확인, 2 뒤로가기"))
            try:
                if thatnono == 1:
                    a.check(list_temp)
                    a.confirm(f,list_temp,choice_list)
                    list_temp = a.confirm1(list_temp)
                    choice_list = a.confirm2(choice_list)
                    break
                elif thatnono == 2:
                    break
                else:
                    print("1~2사이의 값을 입력하세요")
            except:
                print("예약현황이 없습니다.")
                break
    else:
        print("1~4 사이의 값을 입력하여 주세요")
        break
