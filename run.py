import tkinter.messagebox as msgbox

print("접수")
name = input("이름을 입력하세요:")
if not(2 < len(name) < 5):
    print("이름을 다시 확인해주세요.")
    exit()
year,month, day = map(int,input("생년월일을 입력하세요.").split("."))
if not(1900<= year <= 2025 and 1 <= month <= 12 and 1 <= day <= 31):
    print("생년월일을 다시 확인해 주세요:")
    exit()
age = int(input("나이를 입력하세요:"))
if age < 0:
    print("나이는 0세 이상이어야 합니다.")
    exit()
depart = int(input("진료과를 선택하세요(1.내과, 2.외과, 3.소아과, 4.정신과):"))
내과 = []
외과 = []
소아과 = []
정신과 = []

if depart == 1:
    내과.append(name)
    print("내과 접수 완료")
    msgbox.showinfo("알림", "내과 접수 완료")
elif depart == 2:
    외과.append(name)
    print("외과 접수 완료")
    msgbox.showinfo("알림", "외과 접수 완료")
elif depart == 3:
    소아과.append(name)
    print("소아과 접수 완료")
    msgbox.showinfo("알림", "소아과 접수 완료")
elif depart == 4:
    정신과.append(name)
    print("정신과 접수 완료")
    msgbox.showinfo("알림", "정신과 접수 완료")
else:
    print("잘못된 진료과 선택입니다.")

# msgbox.showinfo("알림", "접수 완료")