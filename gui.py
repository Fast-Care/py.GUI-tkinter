import tkinter as tk
from tkinter import messagebox, simpledialog

class PatientCallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("병원 진료 접수")
        self.root.state("zoomed")
        try: self.root.attributes('-zoomed', True)
        except: self.root.attributes('-fullscreen', True)
        self.root.configure(bg="#232946")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=2)
        self.root.grid_columnconfigure(1, weight=1)

        self.진료과목목록 = ["내과", "외과", "소아과", "피부과"]
        self.진료접수목록 = {과목: [] for 과목 in self.진료과목목록}

        self.왼쪽프레임 = tk.Frame(self.root, padx=60, pady=60, bg="#232946")
        self.왼쪽프레임.grid(row=0, column=0, sticky="nsew")
        self.오른쪽프레임 = tk.Frame(self.root, padx=60, pady=60, bg="#eebbc3")
        self.오른쪽프레임.grid(row=0, column=1, sticky="nsew")

        self.라벨목록 = ["이름", "생년월일"]
        self.입력창들 = []
        for i, 텍스트 in enumerate(self.라벨목록):
            tk.Label(self.오른쪽프레임, text=텍스트, font=("Arial", 20, "bold"), bg="#eebbc3", fg="#232946").grid(row=i+1, column=0, sticky="e", pady=20, padx=10)
            입력창 = tk.Entry(self.오른쪽프레임, font=("Arial", 20), width=20, bg="#fffffe", fg="#232946", bd=2, relief="groove")
            입력창.grid(row=i+1, column=1, pady=20, padx=10)
            self.입력창들.append(입력창)

        tk.Label(self.오른쪽프레임, text="성별", font=("Arial", 20, "bold"), bg="#eebbc3", fg="#232946").grid(row=3, column=0, sticky="e", pady=20, padx=10)
        self.성별변수 = tk.StringVar(value="남")
        성별메뉴 = tk.OptionMenu(self.오른쪽프레임, self.성별변수, "남", "여")
        성별메뉴.config(font=("Arial", 20), width=18, bg="#fffffe", fg="#232946", bd=2, relief="groove", highlightthickness=0)
        성별메뉴.grid(row=3, column=1, pady=20, padx=10)

        tk.Label(self.오른쪽프레임, text="진료 과목:", font=("Arial", 20, "bold"), bg="#eebbc3", fg="#232946").grid(row=4, column=0, sticky="e", pady=20, padx=10)
        self.진료과목변수 = tk.StringVar(value="내과")
        진료과목메뉴 = tk.OptionMenu(self.오른쪽프레임, self.진료과목변수, *self.진료과목목록)
        진료과목메뉴.config(font=("Arial", 20), width=18, bg="#fffffe", fg="#232946", bd=2, relief="groove", highlightthickness=0)
        진료과목메뉴.grid(row=4, column=1, pady=20, padx=10)

        tk.Button(self.오른쪽프레임, text="접수 등록", font=("Arial", 20, "bold"), bg="#232946", fg="#eebbc3", activebackground="#393e46", activeforeground="#eebbc3", command=self.접수등록, bd=0, relief="flat"
        ).grid(row=5, column=0, columnspan=2, pady=40, ipadx=40, ipady=15)

        tk.Button(
            self.오른쪽프레임, text="환자 호출", font=("Arial", 20, "bold"),
            bg="#232946", fg="#eebbc3", activebackground="#393e46", activeforeground="#eebbc3",
            command=self.환자호출, bd=0, relief="flat"
        ).grid(row=6, column=0, columnspan=2, pady=10, ipadx=40, ipady=15)

        self.대기명단갱신()

    def 접수등록(self):
        값목록 = [입력창.get().strip() for 입력창 in self.입력창들]
        선택과목 = self.진료과목변수.get()
        성별 = self.성별변수.get()
        if not 값목록[0]:
            messagebox.showwarning("입력 오류", "이름을 입력하세요.")
            return
        if not (값목록[1].isdigit() and len(값목록[1]) == 8):
            messagebox.showwarning("입력 오류", "생년월일을 8자리 숫자로 입력하세요. (예: 20090101)")
            return
        if 성별 not in ["남", "여"]:
            messagebox.showwarning("입력 오류", "성별을 선택하세요.")
            return
        self.진료접수목록[선택과목].append({"이름": 값목록[0], "생년월일": 값목록[1], "성별": 성별})
        messagebox.showinfo("접수 완료", f"{값목록[0]}님 {선택과목} 접수 완료!")
        for 입력창 in self.입력창들: 입력창.delete(0, tk.END)
        self.성별변수.set("남")
        self.대기명단갱신()

    def 대기명단갱신(self):
        for 위젯 in self.왼쪽프레임.winfo_children(): 위젯.destroy()
        tk.Label(self.왼쪽프레임, text="진료 대기 명단", font=("Arial", 26, "bold"), bg="#232946", fg="#eebbc3").pack(anchor="w", pady=(0, 20))
        for 과목 in self.진료과목목록:
            명단 = self.진료접수목록[과목]
            if 명단:
                tk.Label(self.왼쪽프레임, text=f"[{과목}]", font=("Arial", 20, "bold"), fg="#eebbc3", bg="#232946").pack(anchor="w", pady=(10,0))
                for 번호, 항목 in enumerate(명단, 1):
                    tk.Label(self.왼쪽프레임, text=f"  {번호}. {항목['이름']} / {항목['생년월일']} / {항목['성별']}", font=("Arial", 18), fg="#fffffe", bg="#232946").pack(anchor="w", padx=10)

    def 환자호출(self):
        선택과목 = self.진료과목변수.get()
        명단 = self.진료접수목록[선택과목]
        if not 명단:
            messagebox.showinfo("알림", f"{선택과목} 대기 환자가 없습니다.")
            return
        호출환자 = 명단.pop(0)  # 먼저 등록된 환자부터 pop
        self.대기명단갱신()
        호출텍스트 = f"{호출환자['이름']}님\n({호출환자['생년월일']} / {호출환자['성별']})\n{선택과목} 진료실로 들어오세요!"
        호출라벨 = tk.Label(self.root, text=호출텍스트, font=("Arial", 48, "bold"), bg="#f9dcc4", fg="#232946")
        호출라벨.place(relx=0.5, rely=0.5, anchor="center")
        self.root.after(5000, 호출라벨.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientCallApp(root)
    root.mainloop()