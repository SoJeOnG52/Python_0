from tkinter import *
from tkinter import messagebox
def call():
    print("안녕하세요~~ 파이썬 수업 중 입니다~~")
    #messagebox.showinfo("hi~~","파이썬 수업을 재미있게 하자~~!")
    messagebox.showerror("hi~~", "파이썬 수업을 재미있게 하자~~!")

w = Tk()
w.title("1851782 이소정")
w.geometry("250x200")
btnOk =  Button (w, text="확인", command=call)
btnOk.pack()
w.mainloop()