import tkinter as tk
from tkinter import messagebox

진료과목목록 = ["내과", "외과", "소아과", "피부과"]
진료접수목록 = {과목: [] for 과목 in 진료과목목록}

def 접수등록():
    값목록 = [입력창.get() for 입력창 in 입력창들]
    선택과목 = 진료과목변수.get()
    if 값목록[0]:
        진료접수목록[선택과목].append({"이름": 값목록[0], "생년월일": 값목록[1], "성별": 성별변수.get()})
        messagebox.showinfo("접수 완료", f"{값목록[0]}님 {선택과목} 접수 완료!")
        for 입력창 in 입력창들: 입력창.delete(0, tk.END)
        성별변수.set("남")
        대기명단갱신()
    else:
        messagebox.showwarning("입력 오류", "이름을 입력하세요.")

def 대기명단갱신():
    for 위젯 in 왼쪽프레임.winfo_children(): 위젯.destroy()
    tk.Label(왼쪽프레임, text="진료 대기 명단", font=("Arial", 26, "bold"), bg="#232946", fg="#eebbc3").pack(anchor="w", pady=(0, 20))
    for 과목 in 진료과목목록:
        명단 = 진료접수목록[과목]
        if 명단:
            tk.Label(왼쪽프레임, text=f"[{과목}]", font=("Arial", 20, "bold"), fg="#eebbc3", bg="#232946").pack(anchor="w", pady=(10,0))
            for 번호, 항목 in enumerate(명단, 1):
                tk.Label(왼쪽프레임, text=f"  {번호}. {항목['이름']} / {항목['생년월일']} / {항목['성별']}", font=("Arial", 18), fg="#fffffe", bg="#232946").pack(anchor="w", padx=10)

창 = tk.Tk()
창.title("병원 진료 접수")
창.state("zoomed")
try: 창.attributes('-zoomed', True)
except: 창.attributes('-fullscreen', True)
창.configure(bg="#232946")
창.grid_rowconfigure(0, weight=1)
창.grid_columnconfigure(0, weight=2)
창.grid_columnconfigure(1, weight=1)

왼쪽프레임 = tk.Frame(창, padx=60, pady=60, bg="#232946")
왼쪽프레임.grid(row=0, column=0, sticky="nsew")
오른쪽프레임 = tk.Frame(창, padx=60, pady=60, bg="#eebbc3")
오른쪽프레임.grid(row=0, column=1, sticky="nsew")

라벨목록 = ["이름", "생년월일"]
입력창들 = []
for i, 텍스트 in enumerate(라벨목록):
    tk.Label(오른쪽프레임, text=텍스트, font=("Arial", 20, "bold"), bg="#eebbc3", fg="#232946").grid(row=i+1, column=0, sticky="e", pady=20, padx=10)
    입력창 = tk.Entry(오른쪽프레임, font=("Arial", 20), width=20, bg="#fffffe", fg="#232946", bd=2, relief="groove")
    입력창.grid(row=i+1, column=1, pady=20, padx=10)
    입력창들.append(입력창)

tk.Label(오른쪽프레임, text="성별", font=("Arial", 20, "bold"), bg="#eebbc3", fg="#232946").grid(row=3, column=0, sticky="e", pady=20, padx=10)
성별변수 = tk.StringVar(value="남")
성별메뉴 = tk.OptionMenu(오른쪽프레임, 성별변수, "남", "여")
성별메뉴.config(font=("Arial", 20), width=18, bg="#fffffe", fg="#232946", bd=2, relief="groove", highlightthickness=0)
성별메뉴.grid(row=3, column=1, pady=20, padx=10)

tk.Label(오른쪽프레임, text="진료 과목:", font=("Arial", 20, "bold"), bg="#eebbc3", fg="#232946").grid(row=4, column=0, sticky="e", pady=20, padx=10)
진료과목변수 = tk.StringVar(value="내과")
진료과목메뉴 = tk.OptionMenu(오른쪽프레임, 진료과목변수, *진료과목목록)
진료과목메뉴.config(font=("Arial", 20), width=18, bg="#fffffe", fg="#232946", bd=2, relief="groove", highlightthickness=0)
진료과목메뉴.grid(row=4, column=1, pady=20, padx=10)

tk.Button(오른쪽프레임, text="접수 등록", font=("Arial", 20, "bold"), bg="#232946", fg="#eebbc3", activebackground="#393e46", activeforeground="#eebbc3", command=접수등록, bd=0, relief="flat"
).grid(row=5, column=0, columnspan=2, pady=40, ipadx=40, ipady=15)

대기명단갱신()
창.mainloop()