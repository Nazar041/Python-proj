from tkinter import *
from tkinter import messagebox
import pyperclip
import pyshorteners

root = Tk()
root.title("Сокращение ссылок")
root.geometry("400x260")
root["bg"] = "#C3C0C0"

Label(root, text="Добро пожаловать в\nсократер ссылок!", font = "Calibri 15 bold", bg = "#C3C0C0", fg = "#121212").pack(pady=5)
Label(root, text="Введите ссылку:", font = "Calibri 11 bold", bg = "#C3C0C0", fg = "#121212").pack(pady=5)

def click(event):
	link.config(state=NORMAL)
	link.delete(0, END)
link = Entry(root, width=40)
link.insert(0, "Введите силку...")
link.config(state=DISABLED)
link.bind("<Button-1>",click)
link.pack()

Label(root, text="Сокращённая ссылка:", font = "Calibri 11 bold", bg = "#C3C0C0", fg = "#121212").pack(pady=5)

def click(event):
	res.config(state=NORMAL)
	res.delete(0, END)
res = Entry(root, width=40)
res.insert(0, "Сокращённая ссылка")
res.config(state=DISABLED)
res.bind("<Button-1>",click)
res.pack()

def copytoclipboard():
	url = res.get()
	pyperclip.copy(url)

def short():
	try:
		a = link.get()
		s = pyshorteners.Shortener().tinyurl.short(a)
		res.insert(0, s)
	except:
		messagebox.showerror("Сокращение ссылок", "Неверная ссылка!")

Button(root, text="СОКРАТИТЬ", border = 0, bg = "#C5AC2D", fg = "#FFFFFF", font = "Roboto 10 bold", command=short).pack(pady=10)
Button(root, text="КОПИРОВАТЬ", border = 0, bg = "#C5AC2D", fg = "#FFFFFF", font = "Roboto 10 bold", command=copytoclipboard).pack(pady=5)
root.mainloop()