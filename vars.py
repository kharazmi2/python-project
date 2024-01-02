import tkinter
from tkinter import *
root = Tk()
root.title("مدیریت دانش آموز")
root.geometry("800x600")
root.configure(bg="#ffd5ad")
buttons = [Button(root, text="ورود", bg="#2e1600", fg="#ffd5ad"), Button(root, text="نمایش", bg="#2e1600", fg="#ffd5ad")]
labs = [Label(root, text="مدیریت دانش آموز", font=("B Titr", 40), fg="#2e1600", bg="#ffd5ad"), Label(root, text="تهیه شده توسط داس", font=("B Titr", 25), bg="#ffd5ad", fg = "#2e1600")]