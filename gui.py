import tkinter as tk
from tkinter import messagebox

접수목록 = []

def 접수하기():
    이름 = name_entry.get()
    과목 = dept_var.get()
    if 이름:
        접수목록.append({"이름": 이름, "과목": 과목})
        messagebox.showinfo("접수 완료", f"{이름}님 {과목} 접수 완료!")
        name_entry.delete(0, tk.END)
        진료대기명단_업데이트()
    else:
        messagebox.showwarning("입력 오류", "이름을 입력하세요.")

def 진료대기명단_업데이트():
    for widget in left_frame.winfo_children():
        widget.destroy()
    tk.Label(
        left_frame, text="진료 대기 명단",
        font=("Arial", 26, "bold"),
        bg="#232946", fg="#eebbc3"
    ).pack(anchor="w", pady=(0, 20))
    과목별 = {}
    for 항목 in 접수목록:
        과목별.setdefault(항목["과목"], []).append(항목["이름"])
    for 과목, 이름들 in 과목별.items():
        tk.Label(
            left_frame, text=f"[{과목}]",
            font=("Arial", 20, "bold"),
            fg="#eebbc3", bg="#232946"
        ).pack(anchor="w", pady=(10,0))
        for idx, 이름 in enumerate(이름들, start=1):
            tk.Label(
                left_frame, text=f"  {idx}. {이름}",
                font=("Arial", 18),
                fg="#fffffe", bg="#232946"
            ).pack(anchor="w", padx=10)

root = tk.Tk()
root.title("병원 진료 접수")
root.state("zoomed")
try:
    root.attributes('-zoomed', True)
except:
    root.attributes('-fullscreen', True)

root.configure(bg="#232946")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)

left_frame = tk.Frame(root, padx=60, pady=60, bg="#232946")
left_frame.grid(row=0, column=0, sticky="nsew")
right_frame = tk.Frame(root, padx=60, pady=60, bg="#eebbc3", bd=0, relief="flat")
right_frame.grid(row=0, column=1, sticky="nsew")

# 오른쪽: 접수 폼
tk.Label(
    right_frame, text="진료 접수",
    font=("Arial", 26, "bold"),
    bg="#eebbc3", fg="#232946"
).grid(row=0, column=0, columnspan=2, pady=(0, 40))

tk.Label(
    right_frame, text="이름:",
    font=("Arial", 20, "bold"),
    bg="#eebbc3", fg="#232946"
).grid(row=1, column=0, sticky="e", pady=20, padx=10)
name_entry = tk.Entry(right_frame, font=("Arial", 20), width=20, bg="#fffffe", fg="#232946", bd=2, relief="groove")
name_entry.grid(row=1, column=1, pady=20, padx=10)

tk.Label(
    right_frame, text="진료 과목:",
    font=("Arial", 20, "bold"),
    bg="#eebbc3", fg="#232946"
).grid(row=2, column=0, sticky="e", pady=20, padx=10)
dept_var = tk.StringVar(value="내과")
dept_menu = tk.OptionMenu(right_frame, dept_var, "내과", "외과", "소아과", "정형외과")
dept_menu.config(font=("Arial", 20), width=18, bg="#fffffe", fg="#232946", bd=2, relief="groove", highlightthickness=0)
dept_menu.grid(row=2, column=1, pady=20, padx=10)

tk.Button(
    right_frame, text="접수 등록",
    font=("Arial", 20, "bold"),
    bg="#232946", fg="#eebbc3",
    activebackground="#393e46", activeforeground="#eebbc3",
    command=접수하기, bd=0, relief="flat"
).grid(row=3, column=0, columnspan=2, pady=40, ipadx=40, ipady=15)

진료대기명단_업데이트()

root.mainloop()